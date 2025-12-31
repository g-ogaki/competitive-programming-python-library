import Link from "next/link";

export const Header = () => {
  return (
    <header className="flex justify-between items-center p-4 border-b border-gray-200 dark:border-gray-800">
      <Link href="/" className="text-xl font-bold hover:opacity-80 transition-opacity">
        CP Python Library
      </Link>
      <a
        href="https://github.com/g-ogaki/compro_python_library"
        target="_blank"
        rel="noopener noreferrer"
        className="p-2 hover:bg-gray-100 dark:hover:bg-gray-800 rounded-full transition-colors"
        aria-label="GitHub Repository"
      >
        <img
          src="github-mark-white.png"
          alt="GitHub"
          width={24}
          height={24}
          className="w-6 h-6 invert"
        />
      </a>
    </header>
  );
};
