"use client";
import { useState } from "react";
import FileFolder from "./file";

export default function InputFile({ setFileAttached }) {
  function handleFileChange(e) {
    setFileAttached({
      fileVideo: e.target.files[0],
    });
  }
  return (
    <div className="flex items-center justify-center rounded-3xl bg-gray-900/60 max-w-[380px] lg:max-w-[920px] mx-auto p-6 lg:py-20 px-14 lg:px-60 border border-dashed lg:rounded-4xl">
      <div className="flex flex-col justify-center items-center gap-1 text-gray-50">
        <FileFolder />
        <p className="text-base font-medium lg:text-lg">
          Drag and drop file here
        </p>
        <p className="text-sm text-gray-600 font-normal lg:text-base">or</p>
        <input
          onChange={handleFileChange}
          type="file"
          name="fileVideo"
          accept=".mp4"
          className="border border-gray-200 text-sm px-4 py-2 rounded-lg bg-gray-50 w-52 lg:w-60 my-2 text-gray-900"
        />
      </div>
    </div>
  );
}
