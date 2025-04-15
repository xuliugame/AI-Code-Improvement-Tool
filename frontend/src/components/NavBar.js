import React from 'react';
import { AppBar, Toolbar, Typography, Button, Box } from '@mui/material';
import { useAuth } from '../contexts/AuthContext';

// Navigation bar component
const NavBar = () => {
  // Get authentication functions and user data from context
  const { logout, user } = useAuth();
  
  // Handle logout button click
  const handleLogout = () => {
    logout();
  };

  // Render navigation bar
  return (
    <AppBar position="static">
      <Toolbar>
        {/* Application title */}
        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
          AI Code Improvement Tool
        </Typography>
        {/* User information and logout button */}
        {user && (
          <Box sx={{ display: 'flex', alignItems: 'center', gap: 2 }}>
            <Typography>Welcome, {user.username}</Typography>
            <Button color="inherit" onClick={handleLogout}>
              Logout
            </Button>
          </Box>
        )}
      </Toolbar>
    </AppBar>
  );
};

export default NavBar; 