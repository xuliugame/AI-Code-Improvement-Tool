import React, { createContext, useState, useContext, useEffect } from 'react';
import { authService } from '../services/api';

// Create authentication context
const AuthContext = createContext(null);

// Authentication provider component
export const AuthProvider = ({ children }) => {
  // State for user data, loading status, and authentication status
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  // Check authentication status on component mount
  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {
      // If token exists, fetch user profile
      authService.getProfile()
        .then(response => {
          setUser(response.data);
          setIsAuthenticated(true);
        })
        .catch(() => {
          // Clear invalid token and set unauthenticated state
          localStorage.removeItem('token');
          setIsAuthenticated(false);
        })
        .finally(() => {
          setLoading(false);
        });
    } else {
      // No token found, set unauthenticated state
      setIsAuthenticated(false);
      setLoading(false);
    }
  }, []);

  // Login function
  const login = async (username, password) => {
    try {
      // Attempt to login and get token
      const response = await authService.login(username, password);
      localStorage.setItem('token', response.data.access_token);
      // Fetch user profile after successful login
      const profileResponse = await authService.getProfile();
      setUser(profileResponse.data);
      setIsAuthenticated(true);
      return true;
    } catch (error) {
      setIsAuthenticated(false);
      return false;
    }
  };

  // Register function
  const register = async (username, password) => {
    try {
      // Attempt to register new user
      await authService.register(username, password);
      return true;
    } catch (error) {
      return false;
    }
  };

  // Logout function
  const logout = () => {
    // Clear token and user data
    localStorage.removeItem('token');
    setUser(null);
    setIsAuthenticated(false);
  };

  // Provide authentication context to children
  return (
    <AuthContext.Provider value={{ user, login, register, logout, loading, isAuthenticated }}>
      {children}
    </AuthContext.Provider>
  );
};

// Custom hook for using authentication context
export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
}; 