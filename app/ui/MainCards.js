import Image from "next/image";
export default function MainCards() {
  const card = [
    {
      name: "key insights",
      duration: "10s",
    },
    {
      name: "key insights",
      duration: "10s",
    },
    {
      name: "key insights",
      duration: "10s",
    },
  ];
  return (
    <div className="px-8 flex gap-4 items-center justify-center mt-28 lg:my-40 lg:gap-36">
      <div className="w-36 h-40 lg:w-52 lg:h-72 border-gray-200 border-2 rounded-xl shrink-0 absolute -translate-x-2/5 lg:-translate-x-5/6 mr-20 z-30">
        <Image
          className="w-36 h-40 lg:w-52 lg:h-72 object-cover rounded-xl pb-1"
          src={"/1.jpeg"}
          alt="one"
          width={200}
          height={600}
        />
      </div>
      <div className="w-36 h-48 lg:w-58 lg:h-84 border-gray-200 border-2 rounded-xl shrink-0 absolute -translate-x-2/5 lg:-translate-x-3/6 z-40 shadow-horizontal-2xl">
        <Image
          className="w-36 h-48 lg:w-58 lg:h-84 object-cover rounded-xl pb-1"
          src={"/2.jpeg"}
          alt="one"
          width={200}
          height={600}
        />
      </div>
      <div className="w-36 h-60 lg:w-64 lg:h-90 border-gray-200 border-2 rounded-xl shrink-0 absolute z-50 shadow-horizontal-xl">
        <Image
          className="w-36 h-60 lg:w-64 lg:h-90 object-cover rounded-xl pb-1"
          src={"/3.jpeg"}
          alt="one"
          width={200}
          height={600}
        />
      </div>
      <div className="w-36 h-48 lg:w-58 lg:h-84 border-gray-200 border-2 rounded-xl absolute translate-x-1/4 lg:translate-x-2/5 shadow-horizontal-2xl shrink-0 z-40 ml-10">
        <Image
          className="w-36 h-48 lg:w-58 lg:h-84 border-gray-200 border-2 rounded-xl pb-1"
          src={"/4.jpeg"}
          alt="one"
          width={200}
          height={600}
        />
      </div>
      <div className="w-36 h-40 lg:w-52 lg:h-72 border-gray-200 border-2 rounded-xl shrink-0 translate-x-2/4 lg:translate-x-4/5  absolute ml-20 z-30">
        <Image
          className="w-36 h-40 lg:w-52 lg:h-72 border-gray-200 border-2 rounded-xl pb-1"
          src={"/5.jpeg"}
          alt="one"
          width={200}
          height={600}
        />
      </div>
    </div>
  );
}
