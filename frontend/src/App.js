import React, { useState } from 'react';


function App() {
  const [code, setCode] = useState('');
  const [result, setResult] = useState(null);

const handleSubmit = async (e) => {
    e.preventDefault();
    try {
        const response = await fetch("http://127.0.0.1:5000/analyze", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ code })
        });

        const data = await response.json();
        setResult(data.improvements);
    } catch (error) {
        setResult("Error: " + error.message);
    }
};


  return (
    <div className="App">
      <h1>Code Improvement Tool</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          value={code}
          onChange={(e) => setCode(e.target.value)}
          placeholder="Paste your code here..."
          rows={10}
        />
        <button type="submit">Generate Suggestions</button>
      </form>
      {result && (
        <div>
          <h2>Optimization Suggestions</h2>
          <pre>{result}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
