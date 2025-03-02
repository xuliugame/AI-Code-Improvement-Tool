import React from "react";

function Suggestions({ suggestions }) {
  return (
    <div className="suggestions">
      <h2>Optimization Suggestions</h2>
      <p>{suggestions}</p>
    </div>
  );
}

export default Suggestions;
