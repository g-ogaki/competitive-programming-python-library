import Markdown from "react-markdown";
import remarkMath from 'remark-math'
import rehypeKatex from 'rehype-katex'
import 'katex/dist/katex.min.css'

export default function MarkdownRenderer({ children }: { children: string }) {
  return (
    <Markdown
      remarkPlugins={[remarkMath]}
      rehypePlugins={[[rehypeKatex, { fleqn: true }]]}
      components={{
        h1: ({ node, ...props }) => <h1 className="text-3xl font-bold" {...props} />,
        h2: ({ node, ...props }) => <h2 className="text-2xl font-bold py-1 mt-2 border-b-1 border-gray-300" {...props} />,
        h3: ({ node, ...props }) => <h3 className="text-md px-1 font-semibold" {...props} />,
        ul: ({ node, ...props }) => <ul className="list-disc list-inside pl-6" {...props} />,
        ol: ({ node, ...props }) => <ol className="list-decimal list-inside pl-6" {...props} />,
        li: ({ node, ...props }) => <li className="my-1" {...props} />,
        code: ({ node, ...props }) => <code className="bg-gray-100 text-red-500 rounded px-1.5 py-0.5 mr-0.5" {...props} />,
        a: ({ node, ...props }) => <a target="_blank" className="text-blue-600 hover:text-blue-800 visited:text-purple-600" {...props} />,
      }}
    >
      {children}
    </Markdown>);
}