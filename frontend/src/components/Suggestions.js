// Import React and Material-UI components
import React from 'react';
import { Paper, Typography } from '@mui/material';

// Suggestions component for displaying code optimization suggestions
const Suggestions = ({ suggestions }) => {
  // If suggestions are empty, show placeholder
  if (!suggestions) {
    return (
      <div className="box">
        <div className="empty-state">
          <Typography variant="body1" color="textSecondary">
            Enter your code and click "Generate Suggestions" to get optimization recommendations.
          </Typography>
        </div>
      </div>
    );
  }

  // Extract code block from markdown text using regex
  const extractCode = (text) => {
    const codeMatch = text.match(/```(?:\w+)?\n([\s\S]*?)```/);
    return codeMatch ? codeMatch[1].trim() : '';
  };

  // Format suggestion text, automatically style section titles
  const formatSuggestions = (text) => {
    // Remove markdown bold symbols and code blocks
    let cleaned = text.replace(/\*\*/g, '').replace(/```[a-z]*\n[\s\S]*?```/g, '').trim();
    // Use regex to wrap section titles (e.g. 1. Code Analysis) with a styled span
    cleaned = cleaned.replace(/^(\d+\.[^\n]+)/gm, '<span class="suggestion-section-title">$1</span>');
    return cleaned;
  };

  // Convert formatted text to HTML with line breaks
  const createMarkup = (text) => {
    return { __html: text.replace(/\n/g, '<br>') };
  };

  // Extract optimized code from suggestions
  const optimizedCode = extractCode(suggestions);
  
  // Format suggestion text (remove code blocks)
  const formattedSuggestions = formatSuggestions(suggestions);

  return (
    <div className="box" style={{ display: 'flex', flexDirection: 'column', height: '100%' }}>
      <div style={{ 
        display: 'flex', 
        flexDirection: 'column', 
        gap: '2rem',
        height: '100%',
        overflow: 'hidden'
      }}>
        {/* Optimization Suggestions Section */}
        <div style={{ flex: 1, minHeight: 0, display: 'flex', flexDirection: 'column' }}>
          <h1 style={{ 
            fontSize: '1.8rem', 
            fontWeight: '600', 
            color: '#f57c00',
            marginBottom: '1rem',
            flex: 'none'
          }}>
            Optimization Suggestions
          </h1>
          <Paper 
            elevation={0} 
            sx={{ 
              backgroundColor: '#f8f9fa',
              padding: '1.5rem',
              borderRadius: '8px',
              boxShadow: 'inset 0 1px 3px rgba(0, 0, 0, 0.05), 0 1px 2px rgba(0, 0, 0, 0.05)',
              flex: 1,
              overflow: 'auto',
              minHeight: 0
            }}
          >
            <div 
              className="output suggestions-text"
              dangerouslySetInnerHTML={createMarkup(formattedSuggestions)}
            />
          </Paper>
        </div>

        {/* Optimized Code Section */}
        <div style={{ flex: 1, minHeight: 0, display: 'flex', flexDirection: 'column' }}>
          <h1 style={{ 
            fontSize: '1.8rem', 
            fontWeight: '600', 
            color: '#f57c00',
            marginBottom: '1rem',
            flex: 'none'
          }}>
            Optimized Code
          </h1>
          <Paper 
            elevation={0} 
            sx={{ 
              backgroundColor: '#f8f9fa',
              padding: '1.5rem',
              borderRadius: '8px',
              boxShadow: 'inset 0 1px 3px rgba(0, 0, 0, 0.05), 0 1px 2px rgba(0, 0, 0, 0.05)',
              flex: 1,
              overflow: 'auto',
              minHeight: 0
            }}
          >
            <pre className="code-block" style={{ margin: 0 }}>
              {optimizedCode}
            </pre>
          </Paper>
        </div>
      </div>
    </div>
  );
};

export default Suggestions;

// Add style for section titles
const style = document.createElement('style');
style.innerHTML = `
.suggestion-section-title {
  display: block;
  font-size: 1.25em;
  font-weight: bold;
  margin: 1.2em 0 0.5em 0;
  color: #1a1a1a;
}
`;
document.head.appendChild(style);
