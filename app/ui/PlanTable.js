import { Calendar } from "lucide-react";

export default function PlanTable({ fileClips }) {
  const dates = [
    "Monday 7 PM",
    "Tuesday 7 PM",
    "Wendensday 5 PM",
    "Thurday 2 PM",
    "Friday 9 AM",
    "Sunday 11 AM",
    "Saturday 7 PM",
    "Thurday 8 PM",
  ];

  return (
    <div className="bg-gray-900 text-white p-8 max-w-4xl mx-auto rounded-lg">
      <div className="mb-6">
        <div className="flex items-center gap-3 mb-4">
          <Calendar className="text-purple-400" size={32} />
          <h1 className="text-4xl font-bold">
            Plan of <span className="text-purple-400">posting</span>
          </h1>
        </div>

        <p className="text-purple-400 text-lg mb-4">
          This is the viral plan to post those clips
        </p>

        <p className="text-gray-300 text-base leading-relaxed">
          Our AI system has generated an optimized schedule to maximize your
          content reach across platforms. Below is a personalized plan for
          sharing your video clips:
        </p>
      </div>

      {/* Table */}
      <div className="border border-gray-700 rounded-lg overflow-hidden">
        <table className="w-full">
          <thead>
            <tr className="bg-gray-800">
              <th className="text-left p-4 font-semibold text-gray-200">
                Clip
              </th>
              <th className="text-left p-4 font-semibold text-gray-200">
                Clip Description
              </th>
              <th className="text-left p-4 font-semibold text-gray-200">
                Recommended Time Upload
              </th>
              <th className="text-left p-4 font-semibold text-gray-200">
                Hashtags
              </th>
            </tr>
          </thead>
          <tbody>
            {fileClips.descriptions &&
              fileClips.descriptions.map((desc, index) => (
                <tr
                  key={index}
                  className="border-t border-gray-700 hover:bg-gray-800 transition-colors"
                >
                  <td className="p-4 text-white">Clip {index}</td>
                  <td className="p-4 text-white">{desc}</td>
                  <td className="p-4 text-white">{dates[index]}</td>
                  <td className="p-4 text-purple-400">
                    {fileClips.tags[index].join(" ")}
                  </td>
                </tr>
              ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
