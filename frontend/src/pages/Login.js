import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import {
  Box,
  Button,
  TextField,
  Typography,
  Container,
  Paper,
  Alert,
  Snackbar,
} from '@mui/material';
import { orange } from '@mui/material/colors';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const [isRegistering, setIsRegistering] = useState(false);
  const { login, register, isAuthenticated } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    if (isAuthenticated) {
      navigate('/');
    }
  }, [isAuthenticated, navigate]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    e.stopPropagation();
    setError('');
    setSuccess('');

    if (isRegistering) {
      const result = await register(username, password);
      if (result.success) {
        setSuccess('Registration successful! Please login with your credentials.');
        setUsername('');
        setPassword('');
        setIsRegistering(false);
      } else {
        setError(result.error || 'Registration failed');
      }
    } else {
      const result = await login(username, password);
      if (result.success) {
        navigate('/');
      } else {
        setError(result.error || 'Invalid username or password');
      }
    }
  };

  const handleCloseSuccess = () => {
    setSuccess('');
  };

  return (
    <Container component="main" maxWidth="xs">
      <Box
        sx={{
          marginTop: 8,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
        }}
      >
        <Paper
          elevation={3}
          sx={{
            padding: 4,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            width: '100%',
          }}
        >
          <Typography 
            component="h1" 
            variant="h4"
            sx={{ 
              color: orange[700],
              fontWeight: 600,
              fontSize: '2.2rem',
              marginBottom: '1rem'
            }}
          >
            {isRegistering ? 'Register' : 'Login'}
          </Typography>
          {error && (
            <Alert 
              severity="error" 
              sx={{ 
                mt: 2, 
                width: '100%',
                mb: 2
              }}
            >
              {error}
            </Alert>
          )}
          <Box 
            component="form" 
            onSubmit={handleSubmit} 
            sx={{ mt: 1, width: '100%' }}
            noValidate
          >
            <TextField
              margin="normal"
              required
              fullWidth
              id="username"
              label="Username"
              name="username"
              autoComplete="username"
              autoFocus
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              sx={{
                '& .MuiOutlinedInput-root': {
                  '&.Mui-focused fieldset': {
                    borderColor: orange[700],
                  },
                },
                '& .MuiInputLabel-root.Mui-focused': {
                  color: orange[700],
                },
              }}
            />
            <TextField
              margin="normal"
              required
              fullWidth
              name="password"
              label="Password"
              type="password"
              id="password"
              autoComplete="current-password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              sx={{
                '& .MuiOutlinedInput-root': {
                  '&.Mui-focused fieldset': {
                    borderColor: orange[700],
                  },
                },
                '& .MuiInputLabel-root.Mui-focused': {
                  color: orange[700],
                },
              }}
            />
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ 
                mt: 3, 
                mb: 2,
                bgcolor: orange[700],
                '&:hover': {
                  bgcolor: orange[800],
                },
              }}
            >
              {isRegistering ? 'Register' : 'Login'}
            </Button>
            <Button
              fullWidth
              variant="text"
              onClick={() => {
                setIsRegistering(!isRegistering);
                setError('');
                setSuccess('');
                setUsername('');
                setPassword('');
              }}
              sx={{
                color: orange[700],
                '&:hover': {
                  bgcolor: orange[50],
                },
              }}
            >
              {isRegistering
                ? 'Already have an account? Login'
                : "Don't have an account? Register"}
            </Button>
          </Box>
        </Paper>
      </Box>
      <Snackbar
        open={Boolean(success)}
        autoHideDuration={6000}
        onClose={handleCloseSuccess}
        anchorOrigin={{ vertical: 'top', horizontal: 'center' }}
      >
        <Alert 
          onClose={handleCloseSuccess} 
          severity="success" 
          sx={{ 
            width: '100%',
            '& .MuiAlert-icon': {
              color: orange[700],
            },
          }}
        >
          {success}
        </Alert>
      </Snackbar>
    </Container>
  );
};

export default Login; 