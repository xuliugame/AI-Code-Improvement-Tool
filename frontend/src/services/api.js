// Import axios for HTTP requests
import axios from 'axios';

// API base URL
const API_URL = 'http://localhost:5000';

// Create axios instance with default configuration
const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor for adding authentication token
api.interceptors.request.use(
  (config) => {
    // Get token from localStorage
    const token = localStorage.getItem('token');
    if (token) {
      // Add token to Authorization header
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor for handling authentication errors
api.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    // Handle 401 Unauthorized errors
    if (error.response && error.response.status === 401) {
      // Clear token and redirect to login page
      localStorage.removeItem('token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

// Authentication service methods
export const authService = {
  // Register new user
  register: (username, password) => {
    console.log('Registering user:', username);
    return api.post('/register', { username, password });
  },
  // Login user
  login: (username, password) => {
    console.log('Logging in user:', username);
    return api.post('/login', { username, password });
  },
  // Get user profile
  getProfile: () => api.get('/profile'),
};

// Code optimization service methods
export const codeService = {
  // Optimize code
  optimize: (code, language) => api.post('/optimize', { code, language }),
  // Get optimization history
  getHistory: () => api.get('/history'),
  // Delete history entry
  deleteHistory: (id) => api.delete(`/history/${id}`),
};

// Export default axios instance
export default api; 