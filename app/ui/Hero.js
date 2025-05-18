export default function Hero() {
  return (
    <div className="texta flex flex-col gap-3 lg:gap-6 justify-center items-center px-6">
      <div className="text-center flex flex-col gap-2">
        <h1 className="text-white font-semibold text-4xl md:text-5xl lg:text-8xl leading-3.5 lg:leading-18 lg:tracking-tighter">
          Naiza AI, your AI Agent
        </h1>
        <h1 className="gradient-text font-semibold text-4xl md:text-5xl lg:text-8xl lg:tracking-tighter">
          making viral videos
        </h1>
      </div>
      <p className="text-gray-400 font-medium text-center text-sm lg:text-lg">
        Naiza AI extracts the best moments, aka highlights from your videos,
        making short form clips.
      </p>
      <button className="px-4 lg:rounded-3xl  lg:px-8 py-2 lg:py-4 bg-transparent border border-gray-200 font-medium rounded-2xl text-gray-50 lg:text-xl text-xs hover:bg-white hover:text-gray-800 hover:border-white transition-colors lg:my-6">
        Start for free
      </button>
    </div>
  );
}
