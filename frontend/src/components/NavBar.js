import React from 'react';
import { AppBar, Toolbar, Typography, Button } from '@mui/material';
import { orange } from '@mui/material/colors';
import { useAuth } from '../contexts/AuthContext';

// Navigation bar component
const NavBar = () => {
  const { user, logout } = useAuth();
  
  return (
    <AppBar 
      position="static" 
      sx={{ 
        bgcolor: orange[700],
        height: '80px', // Fixed height for navbar
      }}
    >
      <Toolbar sx={{ height: '100%' }}>
        {/* Application title */}
        <Typography 
          variant="h5" 
          component="div" 
          sx={{ 
            flexGrow: 1,
            fontSize: {
              xs: '1.4rem',    // Extra small devices
              sm: '1.6rem',    // Small devices
              md: '1.8rem',    // Medium devices
              lg: '2rem',      // Large devices
              xl: '2.2rem',    // Extra large devices
            },
            fontWeight: 500
          }}
        >
          AI Code Improvement Tool
        </Typography>
        {/* User information and logout button */}
        {user && (
          <>
            <Typography 
              variant="h6" 
              sx={{ 
                mr: 3,
                fontSize: {
                  xs: '1rem',
                  sm: '1.1rem',
                  md: '1.2rem',
                  lg: '1.3rem',
                },
                display: { xs: 'none', sm: 'block' }
              }}
            >
              Welcome, {user.username}
            </Typography>
            <Button 
              color="inherit" 
              onClick={logout}
              sx={{ 
                fontSize: {
                  xs: '0.9rem',
                  sm: '1rem',
                  md: '1.1rem',
                },
                fontWeight: 500,
                px: { xs: 2, sm: 3 },
                py: { xs: 0.5, sm: 0.7 }
              }}
            >
              LOGOUT
            </Button>
          </>
        )}
      </Toolbar>
    </AppBar>
  );
};

export default NavBar; 