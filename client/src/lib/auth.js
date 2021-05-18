import { get } from 'svelte/store';
import { user } from '$lib/stores';
import { auth } from '$lib/stores/auth';
import ax, { refreshAuth } from '$lib/axios';

export const isAuthorized = async (path) => {
  let u = get(user);

  // Preemptively refresh auth token
  if (!get(auth)) {
    try {
      await refreshAuth();
    } catch (_) {
      u = {};
    }
  }

  if (!u.email) {
    try {
      const res = await ax.get('/auth/me');
      user.set(res.data.user);
      u = res.data.user;
    } catch (_) {
      u = {};
    }
  }

  if (!u.email) return false;

  const routePermissions = {
    '/login': ['all'],
    '/register': ['all'],
    '/': ['user'],
    '/profile': ['user']
  };

  const route = routePermissions[path];

  if (route[0] === 'all') return true;

  return route.indexOf(u.type) >= 0;
};
