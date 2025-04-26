// Import axios for HTTP requests
import axios from 'axios';

// Get API base URL based on environment
const getBaseURL = () => {
  if (process.env.NODE_ENV === 'production') {
    // In production (GitHub Pages), use the full backend URL
    return 'https://xuliugame.github.io/AI-Code-Improvement-Tool/api';
  }
  // In development, use the proxy setup from package.json
  return '';
};

// Create axios instance with default configuration
const api = axios.create({
  baseURL: getBaseURL(),
  headers: {
    'Content-Type': 'application/json',
  },
  // Add withCredentials to handle CORS
  withCredentials: true
});

// Add request interceptor to log requests in development
api.interceptors.request.use(request => {
  if (process.env.NODE_ENV === 'development') {
    console.log('Request:', request);
  }
  // Get token from localStorage
  const token = localStorage.getItem('token');
  if (token) {
    // Add token to Authorization header
    request.headers.Authorization = `Bearer ${token}`;
  }
  return request;
}, error => {
  if (process.env.NODE_ENV === 'development') {
    console.error('Request Error:', error);
  }
  return Promise.reject(error);
});

// Add response interceptor to log responses in development
api.interceptors.response.use(response => {
  if (process.env.NODE_ENV === 'development') {
    console.log('Response:', response);
  }
  return response;
}, error => {
  if (process.env.NODE_ENV === 'development') {
    console.error('Response Error:', error);
  }
  // Handle 401 Unauthorized errors
  if (error.response && error.response.status === 401) {
    // Only redirect when not on login page
    if (!window.location.pathname.includes('/login')) {
      localStorage.removeItem('token');
      window.location.href = '/login';
    }
  }
  return Promise.reject(error);
});

// Authentication service methods
export const authService = {
  // Register new user
  register: async (username, password) => {
    try {
      const response = await api.post('/register', { username, password });
      return { success: true, data: response.data };
    } catch (error) {
      return {
        success: false,
        error: error.response?.data?.message || 'Registration failed'
      };
    }
  },
  
  // Login user
  login: async (username, password) => {
    try {
      const response = await api.post('/login', { username, password });
      return { success: true, data: response.data };
    } catch (error) {
      // Do not redirect on login failure
      return {
        success: false,
        error: error.response?.data?.message || 'Invalid username or password'
      };
    }
  },
  
  // Get user profile
  getProfile: () => api.get('/profile'),
};

// Code service methods
export const codeService = {
  // Optimize code
  optimizeCode: (code, language) => {
    return api.post('/optimize', { code, language });
  },
  
  // Get optimization history
  getHistory: () => {
    return api.get('/history');
  },
  
  // Delete history item
  deleteHistory: (id) => {
    return api.delete(`/history/${id}`);
  },
};

// Export default axios instance
export default api; 