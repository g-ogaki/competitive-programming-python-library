import { promises as fs } from "fs";
import path from "path";

export default async function Page() {
  const libraryPath = path.join(process.cwd(), "library");
  const items = await fs.readdir(libraryPath);

  return (
    <div className="max-w-3xl mx-auto py-10 px-4">
      <h1 className="text-3xl font-bold mb-6">Competitive Programming Python Library</h1>
      <p className="text-gray-600 mb-6">Collection of Python algorithms and data structures developed during my competitive programming studies.</p>
      <h2 className="text-2xl font-bold py-1 my-4">Library</h2>
      <div className="bg-white shadow ring-1 ring-black ring-opacity-5 rounded-lg overflow-hidden my-4">
        <div className="px-6 py-5 border-b border-gray-200 bg-gray-50">
          <h3 className="font-semibold text-gray-800">Algorithms / Data Structures</h3>
        </div>
        <ul className="divide-y divide-gray-200">
          {items.map((item) => (
            <li key={item}>
              <a
                href={`${item}`}
                className="flex justify-between items-center px-6 py-4 hover:bg-gray-50 transition-colors duration-150 group"
              >
                <span className="text-sm font-medium text-gray-700 group-hover:text-blue-600">
                  {item.replace(/_/g, " ").replace(/\b\w/g, c => c.toUpperCase())}
                </span>
                <span className="text-xs font-semibold text-blue-600 bg-blue-50 px-2 py-1 rounded-full opacity-0 group-hover:opacity-100 transition-opacity">
                  Open
                </span>
              </a>
            </li>
          ))}
        </ul>
      </div>
      <h2 className="text-2xl font-bold py-1 my-4">Author</h2>
      <ul className="list-disc list-inside pl-6">
        <li className="my-1">AtCoder: <a target="_blank" className="text-blue-600 hover:text-blue-800 visited:text-purple-600" href="https://atcoder.jp/users/moni0627">moni0627</a></li>
        <li className="my-1">Library Checker: <a target="_blank" className="text-blue-600 hover:text-blue-800 visited:text-purple-600" href="https://judge.yosupo.jp/user/onakasuitacity">onakasuitacity</a></li>
      </ul>
      <h2 className="text-2xl font-bold py-1 my-4">License</h2>
      <p className="text-gray-600 mb-6">All code is under CC0 1.0 Universal. See <code className="bg-gray-100 text-red-500 rounded px-1.5 py-0.5 mr-0.5">LICENSE</code> in <a href="https://github.com/g-ogaki/competitive-programming-python-library" target="_blank" className="text-blue-600 hover:text-blue-800 visited:text-purple-600">GitHub</a> for more details.</p>
    </div>
  );
}