import React from 'react';

const Suggestions = ({ suggestions }) => {
  return (
    <div className="box output-box">
      <h2 className="box-title">Optimization Suggestions</h2>
      <pre className="output">{suggestions}</pre>
    </div>
  );
};

export default Suggestions;
