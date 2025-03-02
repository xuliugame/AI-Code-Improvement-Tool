import React, { useState } from "react";
import "./styles.css";

function App() {
  const [code, setCode] = useState("");
  const [suggestions, setSuggestions] = useState("");

  const handleGenerate = async () => {
    setSuggestions("Generating suggestions...");
    try {
      const response = await fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ code }),
      });

      const data = await response.json();
      setSuggestions(data.improvements || "No suggestions returned.");
    } catch (error) {
      setSuggestions("Error generating suggestions.");
    }
  };

  return (
    <div className="page-container">
      <h1 className="title">AI Code Improvement Tool</h1>

      {/* Code Input Box */}
      <div className="box input-box">
        <h2 className="box-title">Enter Your Code</h2>
        <textarea
          className="code-input"
          value={code}
          onChange={(e) => setCode(e.target.value)}
          placeholder="Paste your code here..."
        />
        <button className="generate-btn" onClick={handleGenerate}>
          Generate Suggestions
        </button>
      </div>

      {/* Suggestions Box */}
      <div className="box output-box">
        <h2 className="box-title">Optimization Suggestions</h2>
        <pre className="output">{suggestions}</pre>
      </div>
    </div>
  );
}

export default App;
