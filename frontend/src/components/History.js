import React from 'react';
import { List, ListItem, ListItemText, IconButton, Divider, Paper } from '@mui/material';
import DeleteIcon from '@mui/icons-material/Delete';

// History component for displaying code optimization history
const History = ({ history, onDelete }) => {
  // Function to format the date string
  const formatDate = (dateString) => {
    const date = new Date(dateString);
    const options = {
      year: 'numeric',
      month: '2-digit',
      day: '2-digit',
      hour: '2-digit',
      minute: '2-digit',
      second: '2-digit',
      hour12: true,
      timeZone: Intl.DateTimeFormat().resolvedOptions().timeZone
    };
    return date.toLocaleString('en-US', options);
  };

  // Function to clean text from markdown symbols
  const cleanText = (text) => {
    return text
      .replace(/\*\*/g, '')  // 移除加粗符号
      .replace(/```[a-z]*\n/g, '')  // 移除代码块开始标记
      .replace(/```/g, '')  // 移除代码块结束标记
      .trim();
  };

  return (
    <div className="box history-box">
      <h2 className="box-title">History</h2>
      <List sx={{ 
        width: '100%', 
        bgcolor: 'transparent',
        '& .MuiListItem-root': {
          flexDirection: 'column',
          alignItems: 'stretch',
          bgcolor: '#fff3e0',
          borderRadius: '8px',
          mb: 2,
          p: 2,
          boxShadow: 'inset 0 1px 3px rgba(0, 0, 0, 0.05), 0 1px 2px rgba(0, 0, 0, 0.05)'
        }
      }}>
        {history.map((item) => (
          <React.Fragment key={item.id}>
            <ListItem>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
                <strong style={{ fontSize: '17px', color: '#1a2a3a' }}>
                  {item.language}
                </strong>
                <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
                  <span style={{ color: '#666', fontSize: '14px' }}>
                    {formatDate(item.created_at)}
                  </span>
                  <IconButton 
                    edge="end" 
                    aria-label="delete" 
                    onClick={() => onDelete(item.id)}
                    sx={{ color: '#1a2a3a' }}
                  >
                    <DeleteIcon />
                  </IconButton>
                </div>
              </div>
              <div className="history-content">
                <div className="history-section">
                  <strong className="section-title">Original Code:</strong>
                  <Paper elevation={0} className="code-paper">
                    <pre className="code-block">{cleanText(item.original_code)}</pre>
                  </Paper>
                </div>
                <div className="history-section">
                  <strong className="section-title">Optimization Suggestions:</strong>
                  <Paper elevation={0} className="code-paper">
                    <pre className="code-block">{cleanText(item.optimization_suggestions)}</pre>
                  </Paper>
                </div>
                <div className="history-section">
                  <strong className="section-title">Optimized Code:</strong>
                  <Paper elevation={0} className="code-paper">
                    <pre className="code-block">{cleanText(item.optimized_code)}</pre>
                  </Paper>
                </div>
              </div>
            </ListItem>
          </React.Fragment>
        ))}
      </List>
    </div>
  );
};

export default History; 