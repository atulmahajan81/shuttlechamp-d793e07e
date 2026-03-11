import axios from 'axios';

const apiClient = axios.create({
  baseURL: '/api/v1',
  headers: {
    'Content-Type': 'application/json',
  },
  withCredentials: true,
});

apiClient.interceptors.request.use(config => {
  // Add auth tokens or other custom headers if needed
  return config;
});

apiClient.interceptors.response.use(
  response => response,
  error => {
    if (error.response?.status === 401) {
      // Handle unauthorized errors
      window.location.href = '/auth/login';
    }
    return Promise.reject(error);
  }
);

export default apiClient;