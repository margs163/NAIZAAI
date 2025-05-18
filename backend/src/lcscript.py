from pydantic import BaseModel, Field
# from audio import transcribe_audio_in_chunks, extract_audio
from dotenv import load_dotenv
from langchain_core.tools import StructuredTool
from langchain_groq import ChatGroq
from langchain.tools import tool, BaseTool
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from typing import List, Dict, Union, Any, Annotated, Optional, Tuple, Type, TypedDict
import operator
from langgraph.graph import END, StateGraph, START
from uuid import uuid4
import asyncio
from pprint import pprint
from pathlib import Path

# from langfuse.callback import CallbackHandler
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.2)

classifier_system_prompt = """
You are an AI agent that identifies and extends highlight segments in educational videos for social media content creation. Your goal is to find compelling educational moments and create coherent highlight segments of 15-60 seconds.

Classification Strategy:
Step 1: Initial Classification
Classify each timestamp as potential HIGHLIGHT or NON-HIGHLIGHT based on educational value.
Step 2: Segment Extension
If a timestamp is classified as HIGHLIGHT:
- Extend the highlight backward by 1-2 timestamps for context
- Extend the highlight forward by 2-4 timestamps to complete the educational moment
- Ensure the total segment is 15-60 seconds long
- Merge adjacent highlights into single coherent segments

HIGHLIGHT Criteria for Educational Content:
1. Learning Breakthroughs
"Aha!" moments when students grasp difficult concepts
Successful problem-solving demonstrations
Students connecting ideas or making discoveries
Moments of visible understanding or excitement

2. Engaging Teaching Methods
Creative explanations or analogies
Interactive demonstrations or experiments
Visual aids or props being used effectively
Teacher using humor or storytelling to explain concepts

3. Student Participation & Success
Students actively participating in discussions
Confident student presentations or answers
Collaborative learning moments
Students helping each other understand concepts

4. Practical Applications
Real-world examples being demonstrated
Hands-on activities or experiments
Career connections or industry insights
Skill demonstrations with visible results

5. Emotional Engagement
Students expressing enthusiasm for learning
Moments of surprise or wonder
Overcoming challenges or difficulties
Celebrating achievements or progress

6. Key Educational Content
Core concept explanations (if engaging)
Important formulas or principles being introduced
Critical thinking questions and responses
Summary moments that tie concepts together

NON-HIGHLIGHT Criteria
1. Administrative Content
Attendance taking or housekeeping
Assignment logistics or due dates
Technical difficulties or interruptions
Long silences or wait times

2. Repetitive Content
Reviewing previously covered material (unless adding new insights)
Extended reading from textbooks
Routine practice problems without engagement
Repetitive drilling without interaction

3. Low-Energy Moments
Monotone lectures without interaction
Extended individual work time
Students working silently
Long explanatory monologues without engagement

Guidelines:
Maximum 6 HIGHLIGHT segments - Choose the most compelling educational moments
Segment Length: Aim for 15-60 seconds per highlight segment
Confidence Threshold: >0.7 = HIGHLIGHT, ≤0.7 = NON-HIGHLIGHT
Context Preservation: Always include enough context before and after the core moment
Educational Value: Prioritize content that showcases effective learning and teaching
Social Media Appeal: Consider what would engage viewers and represent your educational mission
"""

classifier_human_prompt = """
{transcriptions}
"""

prompt_agent = ChatPromptTemplate.from_messages(
    [("system", classifier_system_prompt), ("user", classifier_human_prompt)]
)
# Total Groq API transcription time: 3.14s
# [Metadata(timestamp=('00:00:00.160', '00:00:05.120'), confidence_score=0.8, description='Introduction to the concept of unfulfilled potential'),
#  Metadata(timestamp=('00:00:06.160', '00:00:13.020'), confidence_score=0.9, description="Emotional peak: discussing the story of most people's lives"),
#  Metadata(timestamp=('00:00:17.600', '00:00:20.200'), confidence_score=0.7, description="Introduction to the speaker's biggest fear"),
#  Metadata(timestamp=('00:00:22.300', '00:00:28.560'), confidence_score=0.8, description="Discussion of the speaker's biggest fear: not fulfilling their potential"),
#  Metadata(timestamp=('00:01:01.620', '00:01:16.750'), confidence_score=0.9, description="Emotional peak: the speaker's conversation with God about their life"),
#  Metadata(timestamp=('00:01:23.610', '00:01:26.590'), confidence_score=0.8, description="The speaker's realization of their unfulfilled potential"),
#  Metadata(timestamp=('00:01:31.810', '00:01:35.670'), confidence_score=0.7, description="The speaker's fear of judgment"),
#  Metadata(timestamp=('00:01:36.550', '00:01:40.090'), confidence_score=0.8, description="The speaker's desire to fulfill their potential"),
#  Metadata(timestamp=('00:01:41.330', '00:01:44.770'), confidence_score=0.9, description="The speaker's desire to be judged favorably"),
#  Metadata(timestamp=('00:02:12.110', '00:02:18.390'), confidence_score=0.8, description="The speaker's desire to drain their soul of every bit of person they are")]

class Metadata(BaseModel):
    timestamp: Tuple[str, str] = Field(description="Tuple of 'start' and 'end' timestamps")
    confidence_score: float
    description: str = Field(description="Why this moment is a highlight or a non-highlight?")
    tags: List[str] = Field(description="Tags/keywords associated with this moment and to include in an instagram post with this highlight")

class ClassifierOutput(BaseModel):
    highlights: List[Metadata] = Field(
        description="Parts of the transcription with highlights."
    )
    non_highlights: List[Metadata] = Field(
        description="Parts of the transcription with non-highlights."
    )

def seconds_to_precise_timestamp(seconds):
    """Convert seconds to HH:MM:SS.mmm format"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{secs:06.3f}"
    
def parse_transcriptions(transcription: dict):
    result = []
    segments = transcription["segments"]
    for segment in segments:
        result.append(
            (f"TIMESTAMP: ({seconds_to_precise_timestamp(segment['start'])}, {seconds_to_precise_timestamp(segment['end'])})", f"TRANSCRIPTION: {segment['text']}"))
    return result

class State(TypedDict):
    transcriptions: List
    # fluency agent state
    highlight: List 
    non_highlight: List

def overlapping_highlights(h_time: List[tuple[str, str]]):
    h_time_copy = h_time.copy()
    for index, time in enumerate(h_time_copy):
        if (index != len(h_time_copy) - 1):
            print(timestamp_to_seconds(h_time_copy[index + 1][0]), "-", timestamp_to_seconds(time[1]), "=", timestamp_to_seconds(h_time_copy[index + 1][0]) - timestamp_to_seconds(time[1]))
            if timestamp_to_seconds(h_time_copy[index + 1][0]) - timestamp_to_seconds(time[1]) < 8:
                    h_time_copy[index] = (time[0], h_time_copy[index + 1][1])
                    del h_time_copy[index + 1]
    return h_time_copy

def timestamp_to_seconds(timestamp: str) -> float:
    timestamp = timestamp.replace('.', ':')
    parts = timestamp.split(':')
    if len(parts) != 4:
        raise ValueError("Timestamp must be in HH:MM:SS,MMM or HH:MM:SS:MMM format")
    hours, minutes, seconds, milliseconds = map(int, parts)
    total_seconds = hours * 3600 + minutes * 60 + seconds + milliseconds / 1000.0
    return total_seconds

async def classifier_invoke(state: State) -> Dict:
    transcriptions = parse_transcriptions(state['transcriptions'])
    chain = prompt_agent | llm.with_structured_output(ClassifierOutput)
    response: ClassifierOutput = await chain.ainvoke({"transcriptions": transcriptions})
    return {
        "highlight": response.highlights,
        "non_highlight": response.non_highlights,
    }

parallel_graph = StateGraph(State)
parallel_graph.add_node("call_classifier_agent", classifier_invoke)
parallel_graph.add_edge(START, "call_classifier_agent")
parallel_graph.add_edge("call_classifier_agent", END)
app = parallel_graph.compile()

if __name__ == "__main__":
    pass
    async def main():
        extract_audio("./audio/test.mp4", "./audio/output.wav")
        result = transcribe_audio_in_chunks(Path("./audio/output.wav"))
        state = await app.ainvoke({"transcriptions": result})
        pprint(state["highlight"])
        h_time = [time.timestamp for time in state["highlight"]]
        pprint(h_time)
        overlapped_time = overlapping_highlights(h_time)
        pprint(overlapped_time)

    asyncio.run(main())
