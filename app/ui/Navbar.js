import { Menu, X } from "lucide-react";
import Image from "next/image";
import Link from "next/link";

export default function Navbar() {
  return (
    <header className="shadow-sm">
      <nav className="navbar-cont">
        <ul className="flex list-none py-3 px-5 justify-between items-center gap-2 sm:gap-8 md:gap-12 lg:gap-20 text-gray-100">
          <li>
            <Link href="home" className="navlink">
              <div className="flex items-center gap-1">
                {/* <h1 className="hover:text-pink-600 no-underline text-gray-100 text-2xl font-bold py-3 active:bg-neutral-100 cursor-pointer">
                  Shorte
                </h1> */}
                <Image
                  src={"/lgbt(1).png"}
                  alt="something"
                  width={200}
                  height={100}
                  className="w-36"
                />
              </div>
            </Link>
          </li>
          {/* <div
            className={`drop-item transition-all opacity-100 absolute top-0 left-0 z-50 font-semibold text-lg bg-neutral-50 flex flex-col justify-start items-stretch text-center gap-0 w-full h-screen mx-auto ${
              !menuPressed && "hidden"
            } transition-all`}
          >
            <X
              className={`${
                !menuPressed && "hidden"
              } hover:text-indigo-600 text-neutral-800 cursor-pointer self-end mr-5 mt-4 `}
              onClick={() => {
                setMenuPressed(!menuPressed);
              }}
            />
            <Link
              href="about"
              className="hover:text-pink-600 no-underline text-gray-100 font-normal py-3 active:bg-neutral-100 cursor-pointer"
            >
              About
            </Link>
            <Link
              href="contact"
              className="hover:text-pink-600 no-underline text-gray-100 font-normal py-3 active:bg-neutral-100 cursor-pointer"
            >
              Contact
            </Link>
            <Link
              href="works"
              className="hover:text-pink-600 no-underline text-gray-100 font-normal py-3 active:bg-neutral-100 cursor-pointer"
            >
              How It Works
            </Link>
          </div> */}
          <div className="flex items-center gap-8 justify-center ">
            <li className="drop-item hidden ml-auto sm:block">
              <Link
                href="about"
                className="hover:text-pink-700 no-underline text-gray-50 text-base font-normal cursor-pointer transition-colors"
              >
                Product
              </Link>
            </li>
            <li className="drop-item hidden sm:block">
              <Link
                href="about"
                className="hover:text-pink-700 no-underline text-gray-50 text-base font-normal cursor-pointer transition-colors"
              >
                Use Cases
              </Link>
            </li>
            <li className="drop-item hidden sm:block">
              <Link
                href="about"
                className="hover:text-pink-700 no-underline text-gray-50 text-base font-normal cursor-pointer transition-colors"
              >
                How it Works
              </Link>
            </li>
            <li className="drop-item hidden sm:block">
              <Link
                href="contact"
                className="hover:text-pink-600 no-underline text-gray-50 text-base font-normal cursor-pointer transition-colors"
              >
                Benefits
              </Link>
            </li>
            <li className="drop-item hidden sm:block">
              <Link
                href="works"
                className="hover:text-pink-600 no-underline text-gray-50 text-base font-normal cursor-pointer transition-colors"
              >
                FAQ
              </Link>
            </li>
          </div>
          <li className="flex items-center gap-2">
            <Link
              href="login"
              className=" bg-transparent rounded-lg text-sm sm:text-base text-center font-normal py-1 px-3 text-gray-50 hover:bg-white hover:text-gray-800 border border-gray-200 transition-colors"
              id="login-link"
            >
              Book a demo
            </Link>
            <Link
              href="login"
              className=" bg-gray-50 rounded-lg text-sm sm:text-base text-center font-normal py-1 px-3 text-gray-800 hover:bg-pink-600 hover:text-gray-50 transition-colors"
              id="login-link"
            >
              Login
            </Link>
          </li>
        </ul>
      </nav>
    </header>
  );
}
