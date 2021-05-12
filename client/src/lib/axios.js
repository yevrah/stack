import axios from 'axios';
import { get } from 'svelte/store';
import auth from '$lib/stores/auth';

const ax = axios.create({
  baseURL: import.meta.env.VITE_API_URL
});

ax.interceptors.request.use((config) => {
  const au = get(auth);

  if (au) {
    config.headers.Authorization = `Bearer ${au}`;
  }

  return config;
});

export default ax;
