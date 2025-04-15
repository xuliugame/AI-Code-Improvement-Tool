import React from 'react';
import { Box, FormControl, InputLabel, Select, MenuItem, Button } from '@mui/material';

const CodeInput = ({ code, setCode, language, setLanguage, onGenerate }) => {
  return (
    <div className="box input-box">
      <h2 className="box-title">Enter Your Code</h2>
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
      <textarea
        className="code-input"
        value={code}
        onChange={(e) => setCode(e.target.value)}
        placeholder="Paste your code here..."
      />
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
