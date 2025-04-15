import axios from 'axios';

const API_URL = 'http://localhost:5000';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add request interceptor
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Add response interceptor
api.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    if (error.response && error.response.status === 401) {
      localStorage.removeItem('token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

export const authService = {
  register: (username, password) => {
    console.log('Registering user:', username);
    return api.post('/register', { username, password });
  },
  login: (username, password) => {
    console.log('Logging in user:', username);
    return api.post('/login', { username, password });
  },
  getProfile: () => api.get('/profile'),
};

export const codeService = {
  optimize: (code, language) => api.post('/optimize', { code, language }),
  getHistory: () => api.get('/history'),
  deleteHistory: (id) => api.delete(`/history/${id}`),
};

export default api; 