import React from "react";

function CodeInput({ code, setCode }) {
  return (
    <textarea
      className="code-input"
      value={code}
      onChange={(e) => setCode(e.target.value)}
      placeholder="Paste your code here..."
    />
  );
}

export default CodeInput;
