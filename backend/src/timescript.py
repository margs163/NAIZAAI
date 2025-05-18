from typing import Tuple
from moviepy.editor import VideoFileClip, concatenate_videoclips

import os
import glob

def timestamp_includes(container: Tuple[str, str], contained: Tuple[str, str]) -> bool:
    """
    Check if first timestamp period completely includes the second timestamp period
    
    Args:
        container: Tuple of (start_time, end_time) that might contain the other
        contained: Tuple of (start_time, end_time) that might be contained
    
    Returns:
        bool: True if container completely includes contained, False otherwise
    """
    container_start, container_end = container
    contained_start, contained_end = contained
    
    container_start_sec = container[0]
    container_end_sec = container[1]
    contained_start_sec = contained[0]
    contained_end_sec = contained[1]
    
    return (container_start_sec <= contained_start_sec and 
            container_end_sec >= contained_end_sec)

def timestamps_overlap(timestamp1: Tuple[str, str], timestamp2: Tuple[str, str]) -> bool:
    """
    Check if two time periods overlap
    
    Args:
        timestamp1: Tuple of (start_time, end_time) in HH:MM:SS.mmm format
        timestamp2: Tuple of (start_time, end_time) in HH:MM:SS.mmm format
    
    Returns:
        bool: True if the timestamps overlap, False otherwise
    """

    start1, end1 = timestamp1
    start2, end2 = timestamp2
    
    start1_sec = start1
    end1_sec = end1
    start2_sec = start2
    end2_sec = end2
    
    return start1_sec < end2_sec and start2_sec < end1_sec

def combine_videos_moviepy(video_files, output_file):
    """
    Combine multiple video files into one using MoviePy
    
    Args:
        video_files (list): List of video file paths
        output_file (str): Output video file path
    """
    try:
        clips = []
        for video_file in video_files:
            if os.path.exists(video_file):
                clip = VideoFileClip(video_file)
                clips.append(clip)
                print(f"Loaded: {video_file} (Duration: {clip.duration:.2f}s)")
            else:
                print(f"Warning: File not found - {video_file}")
        
        if not clips:
            print("No valid video files found!")
            return False
        
        print("Combining videos...")
        final_clip = concatenate_videoclips(clips)
        
        print(f"Writing output to: {output_file}")
        final_clip.write_videofile(output_file, codec='libx264')
        
        for clip in clips:
            clip.close()
        final_clip.close()
        
        print("Video combination completed successfully!")
        return True
        
    except Exception as e:
        print(f"Error: {e}")
        return False