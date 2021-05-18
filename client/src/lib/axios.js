import { get } from 'svelte/store';
import axios from 'axios';
import createAuthRefreshInterceptor from 'axios-auth-refresh';
import { goto } from '$app/navigation';

import { auth, refresh } from '$lib/stores/auth';

const ax = axios.create({
  baseURL: import.meta.env.VITE_API_URL
});

const refreshAuth = async () => {
  const res = await axios.post(
    '/auth/refresh',
    {},
    {
      headers: { Authorization: `Bearer ${get(refresh)}` },
      baseURL: import.meta.env.VITE_API_URL
    }
  );

  auth.set(res.data.auth_token);

  return res.data.auth_token;
};

const refreshAuthLogic = async (failedRequest) => {
  try {
    const auth_token = await refreshAuth();
    failedRequest.response.config.headers['Authorization'] = `Bearer ${auth_token}`;
  } catch (_) {
    // If the orignal request failed, and we can't refresh the token then we redirect them to login
    await goto('/login');
  }
};

const getToken = () => get(auth);

ax.interceptors.request.use((config) => {
  if (getToken()) config.headers.Authorization = `Bearer ${getToken()}`;
  return config;
});

const onRetry = (requestConfig) => ({ ...requestConfig, baseURL: import.meta.env.VITE_API_URL });

try {
  createAuthRefreshInterceptor(ax, refreshAuthLogic, { onRetry });
} catch (_) {
  // TODO: remove eventually
  // For some reason sveltekit-build thinks `createAuthRefreshInterceptor` is a module
  // and not the exported function.
  // Who knows why but I'm sure it's a bug, so whenever adapter-node is updated, just
  // remove this and check if it builds.
  createAuthRefreshInterceptor.default(ax, refreshAuthLogic, { onRetry });
}

export default ax;
export { refreshAuth };
