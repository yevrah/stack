import ax from '$lib/axios';

export const del = async ({ locals }) => {
  try {
    const res = await ax.delete('/auth/revoke');
    locals.session.destroy = true;

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
