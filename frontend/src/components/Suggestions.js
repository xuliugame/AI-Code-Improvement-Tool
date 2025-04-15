// Import React
import React from 'react';

// Suggestions component for displaying code optimization suggestions
const Suggestions = ({ suggestions }) => {
  return (
    <div className="box output-box">
      <h2 className="box-title">Optimization Suggestions</h2>
      {/* Display suggestions in pre-formatted text */}
      <pre className="output">{suggestions}</pre>
    </div>
  );
};

export default Suggestions;
