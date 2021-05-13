import { initializeSession } from 'svelte-kit-cookie-session';

export const getSession = async ({ locals }) => {
  return locals.session.data;
};

export const handle = async ({ request, render }) => {
  const session = initializeSession(request.headers, {
    secret: import.meta.env.VITE_SECRET_KEY,
    cookie: { path: '/' }
  });

  request.locals.session = session;

  const response = await render(request);

  if (!session['set-cookie']) {
    return response;
  }

  return {
    ...response,
    headers: {
      ...response.headers,
      ...session
    }
  };
};
