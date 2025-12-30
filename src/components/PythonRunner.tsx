"use client";

import { useState } from "react";
import CodeMirror from "@uiw/react-codemirror";
import { python } from "@codemirror/lang-python";
import { indentUnit } from "@codemirror/language";
import { usePython, PythonProvider } from "react-py";

function PythonEditor({ defaultValue }: { defaultValue: string }) {
  const [value, setValue] = useState(defaultValue);
  const { runPython, stdout, stderr, isLoading, isRunning } = usePython();

  return (
    <>
      <h2 className="text-2xl font-bold py-1 mt-2 border-b-1 border-gray-300">Code Test</h2>
      <form className="flex flex-col gap-6">
        <div className="flex flex-col gap-2">
          <CodeMirror
            value={value}
            height="auto"
            minHeight="300px"
            onChange={setValue}
            extensions={[python(), indentUnit.of("    ")]}
          />
          <button
            className="bg-blue-500 hover:bg-blue-600 disabled:bg-gray-400 text-white px-4 py-2 rounded self-start"
            disabled={isLoading || isRunning}
            onClick={(e) => {
              e.preventDefault();
              runPython(value);
            }}
          >
            {isLoading ? "Loading..." : isRunning ? "Running..." : "Run"}
          </button>
        </div>
        <div className="flex flex-col gap-2">
          <label className="font-medium">Standard Output</label>
          <textarea readOnly rows={5} className="bg-gray-200 w-full p-2 font-mono" value={stdout} />
        </div>
        <div className="flex flex-col gap-2">
          <label className="font-medium">Standard Error</label>
          <textarea readOnly rows={5} className="bg-gray-200 w-full p-2 text-red-800 font-mono" value={stderr} />
        </div>
      </form>
    </>
  );
}

export default function PythonRunner({ defaultValue }: { defaultValue: string }) {
  return (
    <PythonProvider packages={{ official: ['pyodide-http'] }}>
      <PythonEditor defaultValue={defaultValue} />
    </PythonProvider>
  );
}