import { Notebook } from "lucide-react";
import FileFolder from "./file";
import { Share } from "next/font/google";
import LineSVG from "./LineSvg";
import ShareSVG from "./ShareSVG";
import NotebookSVG from "./NotebookSVG";

export default function Steps() {
  return (
    <div className="mt-16 lg:mt-20 px-8 flex flex-col gap-10 max-w-[370px] lg:max-w-[920px] mx-auto">
      <div className="flex flex-col gap-2">
        <h2 className="text-2xl font-semibold text-white lg:text-4xl">
          Steps to make your <span className="text-fuchsia-600">viral</span>{" "}
          video
        </h2>
        <p className="text-sm text-gray-400 font-normal lg:text-lg lg:font-medium">
          Turn your long videos into captivating short clips with our AI-powered
          platform, designed to boost engagement on Instagram, Tiktok and
          Youtube
        </p>
      </div>
      <div className="flex flex-col items-start justify-center">
        <div className="flex gap-4 items-start justify-center">
          <FileFolder className="shrink-0" />
          <div className="flex flex-col gap-2 items-start justify-start">
            <h3 className="text-xl lg:text-2xl text-gray-50 font-semibold">
              Step 1.
            </h3>
            <p className="text-sm lg:text-base text-gray-400">
              Upload your video (MP4, MOV, etc.) using our platform's "Upload
              Video" button.
            </p>
          </div>
        </div>
        <div className="pl-6 lg:pl-[1.5rem]">
          <LineSVG />
        </div>
        <div className="flex gap-4 items-start justify-center">
          <NotebookSVG className=" shrink-0" />
          <div className="flex flex-col gap-2 items-start justify-start">
            <h3 className="text-xl lg:text-2xl text-gray-50 font-semibold">
              Step 2.
            </h3>
            <p className="text-sm lg:text-base text-gray-400">
              Upload your video (MP4, MOV, etc.) using our platform's "Upload
              Video" button.
            </p>
          </div>
        </div>
        <div className="pl-6 lg:pl-[1.5rem]">
          <LineSVG />
        </div>
        <div className="flex gap-4 items-start justify-center">
          <ShareSVG />
          <div className="flex flex-col gap-2 items-start justify-start">
            <h3 className="text-xl lg:text-2xl text-gray-50 font-semibold">
              Step 3.
            </h3>
            <p className="text-sm lg:text-base text-gray-400">
              Upload your video (MP4, MOV, etc.) using our platform's "Upload
              Video" button.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
