import { get } from 'svelte/store';
import axios from 'axios';
import createAuthRefreshInterceptor from 'axios-auth-refresh';

import auth from '$lib/stores/auth';

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
  failedRequest.response.config.headers['Authorization'] = `Bearer ${res.data.auth_token}`;
};

const getToken = () => get(auth);

ax.interceptors.request.use((config) => {
  if (getToken()) config.headers.Authorization = `Bearer ${getToken()}`;
  return config;
});

try {
  createAuthRefreshInterceptor(ax, refreshAuthLogic);
} catch (_) {
  // TODO: remove eventually
  // For some reason sveltekit-build thinks `createAuthRefreshInterceptor` is a module
  // and not the exported function.
  // Who knows why but I'm sure it's a bug, so whenever adapter-node is updated, just
  // remove this and check if it builds.
  createAuthRefreshInterceptor.default(ax, refreshAuthLogic);
}

export default ax;
