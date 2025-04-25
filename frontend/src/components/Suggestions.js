// Import React
import React from 'react';
import { Paper, Typography } from '@mui/material';

// Suggestions component for displaying code optimization suggestions
const Suggestions = ({ suggestions }) => {
  // 如果建议为空，显示占位符
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

  // 提取代码块
  const extractCode = (text) => {
    const codeMatch = text.match(/```(?:python)?\n([\s\S]*?)```/);
    return codeMatch ? codeMatch[1].trim() : '';
  };

  // 格式化建议文本
  const formatSuggestions = (text) => {
    return text
      .replace(/\*\*/g, '')  // 移除加粗符号
      .replace(/```[a-z]*\n[\s\S]*?```/g, '')  // 移除所有代码块
      .trim();
  };

  // 将格式化后的文本转换为HTML
  const createMarkup = (text) => {
    return { __html: text.replace(/\n/g, '<br>') };
  };

  // 提取优化后的代码
  const optimizedCode = extractCode(suggestions);
  
  // 格式化建议文本（移除代码块）
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
