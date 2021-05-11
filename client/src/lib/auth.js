const isAuthorized = async ({ page }) => {
  // TODO: fix
  let userType = null;

  const routePermissions = {
    '/': ['user'],
    '/login': ['all'],
    '/register': ['all']
  };

  const route = routePermissions[page.path];

  if (route[0] === 'all') return {};

  return route.indexOf(userType) >= 0 ? {} : { status: 302, redirect: '/login' };
};

export default isAuthorized;
