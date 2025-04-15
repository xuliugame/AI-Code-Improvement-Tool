// Import required React components and modules
import React from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './contexts/AuthContext';
import Login from './pages/Login';
import MainPage from './pages/MainPage';

// PrivateRoute component for protected routes
const PrivateRoute = ({ children }) => {
  const { isAuthenticated, loading } = useAuth();
  
  // Show loading state while checking authentication
  if (loading) {
    return <div>Loading...</div>;
  }
  
  // Redirect to login if not authenticated, otherwise render children
  return isAuthenticated ? children : <Navigate to="/login" />;
};

// Main App component
const App = () => {
  return (
    // Wrap the entire app with AuthProvider for authentication context
    <AuthProvider>
      <Router>
        <Routes>
          {/* Public route for login page */}
          <Route path="/login" element={<Login />} />
          
          {/* Protected route for main page */}
          <Route
            path="/"
            element={
              <PrivateRoute>
                <MainPage />
              </PrivateRoute>
            }
          />
          
          {/* Catch-all route that redirects to home */}
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </Router>
    </AuthProvider>
  );
};

export default App;
