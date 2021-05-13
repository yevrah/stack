import axios from 'axios';

export const post = async ({ locals, body }) => {
  try {
    const res = await axios.post('/auth/token', body, { baseURL: import.meta.env.VITE_API_URL });
    locals.session.data = { refresh_token: res.data.refresh_token };

    return {
      body: res.data
    };
  } catch (e) {
    if (e.response) {
      return {
        status: e.response.data.status,
        body: e.response.data
      };
    } else {
      return {
        status: 500,
        body: { msg: e.message }
      };
    }
  }
};
