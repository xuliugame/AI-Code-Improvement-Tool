import React from 'react';
import { FormControl, InputLabel, Select, MenuItem, Button, Box, CircularProgress } from '@mui/material';
import { orange } from '@mui/material/colors';
import ClearIcon from '@mui/icons-material/Clear';

const CodeInput = ({ code, setCode, language, setLanguage, onGenerate, isLoading }) => {
  const handleClear = () => {
    setCode('');
  };

  return (
    <div className="box input-box">
      <h2 className="box-title">Enter Your Code</h2>
      <div className="input-box-content">
        <Box sx={{ width: '100%', display: 'flex', flexDirection: 'column', flex: 1 }}>
          {/* Language selection dropdown */}
          <FormControl fullWidth>
            <InputLabel id="language-select-label">Language</InputLabel>
            <Select
              labelId="language-select-label"
              id="language-select"
              value={language}
              label="Language"
              onChange={(e) => setLanguage(e.target.value)}
              disabled={isLoading}
              sx={{
                '&.Mui-focused .MuiOutlinedInput-notchedOutline': {
                  borderColor: orange[700],
                },
                marginBottom: '1rem'
              }}
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
            disabled={isLoading}
          />
          {/* Buttons container */}
          <div className="button-container" style={{ display: 'flex', gap: '1rem' }}>
            <Button
              variant="contained"
              onClick={onGenerate}
              disabled={isLoading}
              sx={{ 
                flex: 1,
                bgcolor: orange[700],
                '&:hover': {
                  bgcolor: orange[800],
                },
                '&.Mui-disabled': {
                  bgcolor: orange[200],
                  color: 'rgba(0, 0, 0, 0.26)'
                }
              }}
            >
              {isLoading ? (
                <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                  <CircularProgress size={20} color="inherit" />
                  <span>Analyzing Code...</span>
                </Box>
              ) : (
                'Generate Suggestions'
              )}
            </Button>
            {code && !isLoading && (
              <Button
                variant="outlined"
                onClick={handleClear}
                sx={{
                  borderColor: orange[700],
                  color: orange[700],
                  '&:hover': {
                    borderColor: orange[800],
                    bgcolor: 'rgba(245, 124, 0, 0.04)',
                  },
                }}
                startIcon={<ClearIcon />}
              >
                Clear
              </Button>
            )}
          </div>
        </Box>
      </div>
    </div>
  );
};

export default CodeInput;
