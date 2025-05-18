import Image from "next/image";
import Hero from "./ui/Hero";
import MainCards from "./ui/MainCards";
import Steps from "./ui/Steps";

export default function Home() {
  return (
    <div className="my-8 lg:my-20">
      <main className="flex flex-col gap-12 lg:gap-20">
        <Hero />
        <MainCards />
        <Steps />
      </main>
    </div>
  );
}
