"use client";
import { Skeleton } from "@/components/ui/skeleton";
export default function Clips({ fileClips }) {
  return (
    <div className="flex flex-col gap-6 lg:gap-10 max-w-[370px] lg:max-w-[920px] mx-auto p-6 lg:p-12">
      <h2 className="text-3xl font-semibold text-gray-50 pl-2 lg:text-4xl">
        Generated <span className="text-fuchsia-600">clips</span>
      </h2>
      {!fileClips.paths ? (
        <div className="w-full flex flex-wrap gap-6 lg:gap-8 items-center justify-center">
          {[0, 1, 2, 3, 4, 5].map((item) => {
            return (
              <Skeleton
                key={item}
                className={
                  "w-[150px] lg:w-[250px] lg:h-[400px] h-[250px] rounded-lg gradient-background"
                }
              />
            );
          })}
        </div>
      ) : (
        <div className="w-full flex flex-wrap gap-6 lg:gap-8 items-center justify-center">
          {fileClips.paths &&
            fileClips.paths.map((item, index) => {
              return (
                <div
                  key={index}
                  className="w-[265px] lg:w-[400px] lg:h-[225px] h-[135px] rounded-lg border-2 border-gray-200"
                >
                  <video
                    src={item}
                    className="object-fill rounded-lg"
                    controls
                  />
                </div>
              );
            })}
        </div>
      )}
    </div>
  );
}
