import React from 'react';
import { List, ListItem, ListItemText, IconButton, Divider } from '@mui/material';
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

  return (
    <div className="box history-box">
      <h2 className="box-title">History</h2>
      {/* List of history items */}
      <List sx={{ width: '100%', bgcolor: 'background.paper' }}>
        {history.map((item) => (
          <React.Fragment key={item.id}>
            <ListItem
              // Delete button for each history item
              secondaryAction={
                <IconButton edge="end" aria-label="delete" onClick={() => onDelete(item.id)}>
                  <DeleteIcon />
                </IconButton>
              }
            >
              <ListItemText
                // Display language and timestamp
                primary={`${item.language} - ${formatDate(item.created_at)}`}
                // Display original and optimized code
                secondary={
                  <div>
                    <div><strong>Original Code:</strong></div>
                    <pre style={{ margin: '5px 0' }}>{item.original_code}</pre>
                    <div><strong>Optimized Code:</strong></div>
                    <pre style={{ margin: '5px 0' }}>{item.optimized_code}</pre>
                  </div>
                }
              />
            </ListItem>
            {/* Divider between history items */}
            <Divider component="li" />
          </React.Fragment>
        ))}
      </List>
    </div>
  );
};

export default History; 