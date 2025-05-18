"use client";
import { useEffect, useRef, useState } from "react";
import InputFile from "../ui/InputFile";
import Clips from "../ui/clips";
import AutoPosting from "../ui/AutoPosting";
import PlanTable from "../ui/PlanTable";

export default function page() {
  const [fileClips, setFileClips] = useState({
    paths: null,
    descriptions: null,
    tags: null,
  });
  const [fileAttached, setFileAttached] = useState({
    fileVideo: null,
  });
  const [uploadFormData, setUploadFormData] = useState({
    login: "",
    password: "",
    video_path: "",
    video_caption: "",
  });
  const websocketRef = useRef(null);

  async function handleSubmitForm(e) {
    e.preventDefault();
  }

  useEffect(() => {
    async function fetchClips() {
      websocketRef.current = new WebSocket(`ws://localhost:8000/highlight/ws`);

      websocketRef.current.addEventListener("message", (event) => {
        const { filenames, descriptions, tags } = JSON.parse(event.data);
        setFileClips({
          paths: filenames,
          descriptions: descriptions,
          tags: tags,
        });
      });

      if (fileAttached.fileVideo) {
        const formData = new FormData();
        formData.append("video_file", fileAttached.fileVideo);
        const response = await fetch("http://localhost:8000/highlight", {
          method: "POST",
          body: formData,
          headers: {
            accept: "application/json",
          },
        });

        if (!response.ok) {
          throw new Error("Error in file request");
        }

        websocketRef.current.send("order_69");
      }
    }

    fetchClips();
  }, [fileAttached]);
  return (
    <div className="my-8 lg:my-20 flex flex-col gap-14">
      <InputFile setFileAttached={setFileAttached} />
      <Clips fileClips={fileClips} />
      <PlanTable fileClips={fileClips} />
      <AutoPosting
        fileClips={fileClips}
        uploadFormData={uploadFormData}
        setUploadFormData={setUploadFormData}
      />
    </div>
  );
}
