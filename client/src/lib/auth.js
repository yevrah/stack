import { get } from 'svelte/store';
import { user } from '$lib/stores';
import ax from '$lib/axios';

export const isAuthorized = async (path) => {
  let u = get(user);

  if (!u.email) {
    try {
      const res = await ax.get('/auth/me');
      user.set(res.data.user);
      u = res.data.user;
    } catch (_) {
      u = {};
    }
  }

  const routePermissions = {
    '/': ['user'],
    '/login': ['all'],
    '/register': ['all']
  };

  const route = routePermissions[path];

  if (route[0] === 'all') return true;

  return route.indexOf(u.type) >= 0;
};
