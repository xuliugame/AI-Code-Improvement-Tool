// Import React
import React from 'react';
import { Paper, Typography } from '@mui/material';

// Suggestions component for displaying code optimization suggestions
const Suggestions = ({ suggestions }) => {
  // 如果建议为空，显示占位符
  if (!suggestions) {
    return (
      <div className="box output-box">
        <h2 className="box-title">Optimization Suggestions</h2>
        <div className="empty-state">
          <Typography variant="body1" color="textSecondary">
            Enter your code and click "Generate Suggestions" to get optimization recommendations.
          </Typography>
        </div>
      </div>
    );
  }

  // 格式化建议文本
  const formatSuggestions = (text) => {
    // 移除 Markdown 符号并格式化文本
    let formattedText = text
      .replace(/\*\*/g, '')  // 移除加粗符号
      .replace(/```[a-z]*\n/g, '')  // 移除代码块开始标记
      .replace(/```/g, '')  // 移除代码块结束标记
      .trim();

    // 处理特定标题的加粗
    formattedText = formattedText
      .replace(/^Optimized Version:/gm, '<strong>Optimized Version:</strong>')
      .replace(/^Why is this better\?/gm, '<strong>Why is this better?</strong>')
      .replace(/^Summary:/gm, '<strong>Summary:</strong>')
      .replace(/^Further Optimization with Generators/gm, '<strong>Further Optimization with Generators</strong>');

    // 如果文本包含分节标记，进行格式化
    const parts = formattedText.split('2) Optimized Code');
    if (parts.length === 2) {
      const suggestions = parts[0].replace('1) Optimization Suggestions', '').trim();
      const optimizedCode = parts[1].trim();
      
      return `<strong>Optimization Suggestions:</strong>\n\n${suggestions}\n\n<strong>Optimized Code:</strong>\n\n${optimizedCode}`;
    }
    
    return formattedText;
  };

  // 将格式化后的文本转换为HTML
  const createMarkup = (text) => {
    return { __html: text.replace(/\n/g, '<br>') };
  };

  return (
    <div className="box output-box">
      <h2 className="box-title">Optimization Suggestions</h2>
      <Paper elevation={0} className="suggestions-content">
        <div 
          className="output suggestions-text"
          dangerouslySetInnerHTML={createMarkup(formatSuggestions(suggestions))}
        />
      </Paper>
    </div>
  );
};

export default Suggestions;
