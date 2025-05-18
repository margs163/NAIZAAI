import { Instagram, Twitter, Youtube } from "lucide-react";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
  DialogClose,
} from "@/components/ui/dialog";

export default function AutoPosting({
  fileClips,
  uploadFormData,
  setUploadFormData,
}) {
  function handleSelectChange(value) {
    setUploadFormData((prev) => {
      return {
        ...prev,
        video_path: value,
      };
    });
  }

  function handleInput(e) {
    setUploadFormData((prev) => {
      return {
        ...prev,
        [e.target.name]: e.target.value,
      };
    });
  }
  return (
    <div className="max-w-[380px] lg:max-w-[920px] lg:gap-6 lg:px-12 mx-auto flex flex-col gap-4 px-6">
      <div className="flex flex-col gap-2">
        <h2 className="text-2xl lg:text-4xl font-semibold text-gray-50">
          Auto-<span className=" text-fuchsia-600">Posting</span>
        </h2>
        <div>
          <h3 className="gradient-text lg:text-xl text-lg font-medium">
            This is the viral plan to post those clips
          </h3>
          <p className="text-gray-400 font-medium text-xs lg:text-base">
            Our Al system has generated an optimized schedule to maximize your
            content reach across platforms. Below is a personalized plan for
            sharing your video clips:
          </p>
        </div>
      </div>
      <div className="flex flex-wrap gap-4 lg:gap-6 lg:mt-4">
        <Dialog>
          <DialogTrigger asChild>
            <button className="px-2 py-1 lg:px-4 lg:py-2 text-gray-50 text-xs lg:text-sm pl-2 font-medium flex gap-2 border-gray-200 border rounded-xl items-center">
              <Instagram size={18} />
              Post on Instagram
            </button>
          </DialogTrigger>
          <DialogContent className="max-w-[350px] bg-white rounded-lg">
            <DialogHeader className={"flex justify-start text-start"}>
              <DialogTitle>Create a New Topic</DialogTitle>
              <DialogDescription>
                Make changes to your profile here. Click save when you're done.
              </DialogDescription>
            </DialogHeader>
            <form
              onSubmit={(e) => onCreateTopic(e)}
              className="flex flex-col gap-4"
            >
              {fileClips.paths && (
                <div className="flex flex-col gap-1">
                  <label
                    htmlFor="video-select"
                    className="text-gray-700 text-sm"
                  >
                    Video Path
                  </label>
                  <select
                    onChange={handleSelectChange}
                    id="video-select"
                    className="border border-gray-200 text-sm px-4 py-2 rounded-lg bg-white"
                    name="video_path"
                  >
                    {fileClips.paths.map((item, index) => {
                      return <option value={item}>Video Clip {index}</option>;
                    })}
                  </select>
                </div>
              )}
              <div className="flex flex-col gap-1">
                <label
                  htmlFor="video-caption"
                  className=" text-gray-700 text-sm"
                >
                  Video Captions
                </label>
                <input
                  onChange={handleInput}
                  value={uploadFormData.video_captions}
                  placeholder="Enter a video caption..."
                  id="video-caption"
                  name="video_caption"
                  className="border border-gray-200 text-sm px-4 py-2 rounded-lg"
                  required
                />
              </div>
              <div className="flex flex-col gap-1">
                <label htmlFor="login-name" className=" text-gray-700 text-sm">
                  Login
                </label>
                <input
                  onChange={handleInput}
                  value={uploadFormData.login}
                  id="login-name"
                  name="login"
                  placeholder="Enter your login..."
                  className="border border-gray-200 text-sm px-4 py-2 rounded-lg"
                  required
                />
              </div>
              <div className="flex flex-col gap-1">
                <label htmlFor="password" className=" text-gray-700 text-sm">
                  password
                </label>
                <input
                  onChange={handleInput}
                  value={uploadFormData.password}
                  id="password"
                  name="password"
                  placeholder="Enter your password..."
                  className="border border-gray-200 text-sm px-4 py-2 rounded-lg"
                  type="password"
                  required
                />
              </div>
              <div className="flex self-end gap-3 justify-start mt-4">
                <DialogClose asChild>
                  <button className="bg-gray-400 px-4 py-2 rounded-lg text-white font-medium text-sm hover:bg-gray-500">
                    Cancel
                  </button>
                </DialogClose>
                <DialogClose asChild>
                  <button
                    type="submit"
                    className="bg-gray-800 px-4 py-2 rounded-lg text-white font-medium text-sm hover:bg-gray-900"
                  >
                    Create
                  </button>
                </DialogClose>
              </div>
            </form>
          </DialogContent>
        </Dialog>
        <button className="px-2 py-1 lg:px-4 lg:py-2 text-gray-50 pl-2 lg:text-sm font-medium flex text-xs gap-2 border-gray-200 border rounded-xl items-center">
          <Youtube />
          Post on Youtube
        </button>
        <button className="px-2 py-1 lg:px-4 lg:py-2 lg:text-sm text-gray-50 pl-2 font-medium flex text-xs items-center gap-2 border-gray-200 border rounded-xl">
          <Twitter />
          Post on Twitter
        </button>
      </div>
    </div>
  );
}
