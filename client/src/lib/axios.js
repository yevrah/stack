import axios from 'axios';
import createAuthRefreshInterceptor from 'axios-auth-refresh';

axios.defaults.baseURL = import.meta.env.VITE_API_URL;

const ax = axios.create();

const refreshAuthLogic = async (failedRequest) => {
  const refresh = localStorage.getItem('refresh_token') || '';

  const res = await axios.post(
    '/auth/refresh',
    {},
    { headers: { Authorization: `Bearer ${refresh}` } }
  );

  localStorage.setItem('auth_token', res.data.auth_token);
  failedRequest.response.config.headers['Authorization'] = 'Bearer ' + res.data.auth_token;
  return;
};

const getToken = () => localStorage.getItem('auth_token');

ax.interceptors.request.use((config) => {
  if (getToken()) config.headers.Authorization = `Bearer ${getToken()}`;
  return config;
});

createAuthRefreshInterceptor(ax, refreshAuthLogic);

export default ax;
