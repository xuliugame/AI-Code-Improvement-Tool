import React from 'react';
import { FormControl, InputLabel, Select, MenuItem, Button } from '@mui/material';

// Code input component for entering and selecting code
const CodeInput = ({ code, setCode, language, setLanguage, onGenerate }) => {
  return (
    <div className="box input-box">
      <h2 className="box-title">Enter Your Code</h2>
      {/* Language selection dropdown */}
      <FormControl fullWidth sx={{ mb: 2 }}>
        <InputLabel id="language-select-label">Language</InputLabel>
        <Select
          labelId="language-select-label"
          id="language-select"
          value={language}
          label="Language"
          onChange={(e) => setLanguage(e.target.value)}
        >
          <MenuItem value="python">Python</MenuItem>
          <MenuItem value="javascript">JavaScript</MenuItem>
          <MenuItem value="java">Java</MenuItem>
          <MenuItem value="cpp">C++</MenuItem>
        </Select>
      </FormControl>
      {/* Code input textarea */}
      <textarea
        className="code-input"
        value={code}
        onChange={(e) => setCode(e.target.value)}
        placeholder="Paste your code here..."
      />
      {/* Generate suggestions button */}
      <Button 
        variant="contained" 
        onClick={onGenerate}
        sx={{ mt: 2 }}
      >
        Generate Suggestions
      </Button>
    </div>
  );
};

export default CodeInput;
