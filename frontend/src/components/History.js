import React from 'react';
import { List, IconButton, Paper } from '@mui/material';
import DeleteIcon from '@mui/icons-material/Delete';
import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown';
import KeyboardArrowUpIcon from '@mui/icons-material/KeyboardArrowUp';

// History component for displaying code optimization history
const History = ({ history, onDelete }) => {
  // State for tracking which history item is expanded
  const [expandedId, setExpandedId] = React.useState(null);

  // Format date string to a readable format
  const formatDate = (dateString) => {
    const date = new Date(dateString);
    return date.toLocaleString('en-US', {
      year: 'numeric',
      month: '2-digit',
      day: '2-digit',
      hour: '2-digit',
      minute: '2-digit',
      hour12: false
    });
  };

  // Clean text by removing markdown symbols
  const cleanText = (text) => {
    return text
      .replace(/\*\*/g, '')  // Remove bold symbols
      .replace(/```[a-z]*\n/g, '')  // Remove code block start markers
      .replace(/```/g, '')  // Remove code block end markers
      .trim();
  };

  // Toggle expansion state of a history item
  const handleExpand = (id) => {
    setExpandedId(expandedId === id ? null : id);
  };

  return (
    <div className="box history-box">
      <h2 className="box-title">History</h2>
      <List sx={{ width: '100%', bgcolor: 'transparent', py: 0 }}>
        {history.map((item) => (
          <Paper
            key={item.id}
            sx={{
              mb: 1.5,
              overflow: 'hidden',
              bgcolor: '#f8f9fa',
              borderRadius: '8px',
              border: '1px solid rgba(0, 0, 0, 0.05)'
            }}
          >
            {/* History item header with language and actions */}
            <div
              onClick={() => handleExpand(item.id)}
              style={{
                display: 'flex',
                flexDirection: 'column',
                padding: '12px 16px',
                cursor: 'pointer',
                borderBottom: expandedId === item.id ? '1px solid rgba(0, 0, 0, 0.05)' : 'none'
              }}
            >
              {/* Top row with language and actions */}
              <div style={{
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'space-between',
                marginBottom: '8px'
              }}>
                <div style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: '12px'
                }}>
                  {/* Language badge */}
                  <div style={{
                    backgroundColor: '#1a2a3a',
                    color: '#fff',
                    padding: '2px 8px',
                    borderRadius: '4px',
                    fontSize: '13px',
                    fontWeight: 500
                  }}>
                    {item.language}
                  </div>
                  {/* Timestamp */}
                  <span style={{ color: '#666', fontSize: '13px' }}>
                    {formatDate(item.created_at)}
                  </span>
                </div>
                {/* Action buttons */}
                <div style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: '12px'
                }}>
                  {/* Delete button */}
                  <IconButton
                    size="small"
                    onClick={(e) => {
                      e.stopPropagation();
                      onDelete(item.id);
                    }}
                    sx={{
                      color: '#666',
                      padding: '4px',
                      '&:hover': {
                        color: '#d32f2f',
                        backgroundColor: 'rgba(211, 47, 47, 0.04)'
                      }
                    }}
                  >
                    <DeleteIcon fontSize="small" />
                  </IconButton>
                  {/* Expand/collapse button */}
                  {expandedId === item.id ? 
                    <KeyboardArrowUpIcon sx={{ color: '#666', fontSize: 20 }} /> : 
                    <KeyboardArrowDownIcon sx={{ color: '#666', fontSize: 20 }} />
                  }
                </div>
              </div>
              {/* Code preview */}
              <div style={{
                fontFamily: "'Fira Code', monospace",
                fontSize: '13px',
                color: '#1a2a3a',
                backgroundColor: '#fff',
                padding: '12px',
                borderRadius: '4px',
                whiteSpace: 'pre-wrap'
              }}>
                {cleanText(item.original_code)}
              </div>
            </div>

            {/* Expanded content section */}
            {expandedId === item.id && (
              <div style={{ padding: '16px', backgroundColor: '#fff' }}>
                <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
                  {/* Original code section */}
                  <div>
                    <div style={{
                      fontSize: '13px',
                      fontWeight: 600,
                      color: '#1a2a3a',
                      marginBottom: '8px'
                    }}>
                      Original Code
                    </div>
                    <Paper
                      elevation={0}
                      sx={{
                        backgroundColor: '#f8f9fa',
                        padding: '12px',
                        borderRadius: '4px'
                      }}
                    >
                      <pre style={{
                        margin: 0,
                        fontFamily: "'Fira Code', monospace",
                        fontSize: '13px',
                        lineHeight: 1.5,
                        color: '#0066cc'
                      }}>
                        {cleanText(item.original_code)}
                      </pre>
                    </Paper>
                  </div>
                  {/* Optimization suggestions section */}
                  <div>
                    <div style={{
                      fontSize: '13px',
                      fontWeight: 600,
                      color: '#1a2a3a',
                      marginBottom: '8px'
                    }}>
                      Optimization Suggestions
                    </div>
                    <Paper
                      elevation={0}
                      sx={{
                        backgroundColor: '#f8f9fa',
                        padding: '12px',
                        borderRadius: '4px'
                      }}
                    >
                      <pre style={{
                        margin: 0,
                        fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
                        fontSize: '13px',
                        lineHeight: 1.6,
                        color: '#1a2a3a',
                        whiteSpace: 'pre-wrap'
                      }}>
                        {cleanText(item.optimization_suggestions)}
                      </pre>
                    </Paper>
                  </div>
                  {/* Optimized code section */}
                  <div>
                    <div style={{
                      fontSize: '13px',
                      fontWeight: 600,
                      color: '#1a2a3a',
                      marginBottom: '8px'
                    }}>
                      Optimized Code
                    </div>
                    <Paper
                      elevation={0}
                      sx={{
                        backgroundColor: '#f8f9fa',
                        padding: '12px',
                        borderRadius: '4px'
                      }}
                    >
                      <pre style={{
                        margin: 0,
                        fontFamily: "'Fira Code', monospace",
                        fontSize: '13px',
                        lineHeight: 1.5,
                        color: '#0066cc'
                      }}>
                        {cleanText(item.optimized_code)}
                      </pre>
                    </Paper>
                  </div>
                </div>
              </div>
            )}
          </Paper>
        ))}
      </List>
    </div>
  );
};

export default History; 