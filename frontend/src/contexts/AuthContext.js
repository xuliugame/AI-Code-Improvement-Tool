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
          setUser(null);
        })
        .finally(() => {
          setLoading(false);
        });
    } else {
      // No token found, set unauthenticated state
      setIsAuthenticated(false);
      setUser(null);
      setLoading(false);
    }
  }, []);

  // Login function
  const login = async (username, password) => {
    try {
      const result = await authService.login(username, password);
      
      if (result.success) {
        localStorage.setItem('token', result.data.access_token);
        setUser(result.data.user);
        setIsAuthenticated(true);
      }
      
      return result; // 返回完整的结果对象
    } catch (error) {
      console.error('Login error:', error);
      return {
        success: false,
        error: 'An unexpected error occurred during login'
      };
    }
  };

  // Register function
  const register = async (username, password) => {
    try {
      const result = await authService.register(username, password);
      return result; // Just return the result, don't auto-login
    } catch (error) {
      console.error('Registration error:', error);
      return {
        success: false,
        error: 'An unexpected error occurred during registration'
      };
    }
  };

  // Logout function
  const logout = () => {
    localStorage.removeItem('token');
    setUser(null);
    setIsAuthenticated(false);
  };

  // Provide authentication context to children
  return (
    <AuthContext.Provider value={{
      user,
      login,
      register,
      logout,
      loading,
      isAuthenticated
    }}>
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