export async function del({ locals }) {
  locals.session.destroy = true;

  return {
    body: {
      ok: true
    }
  };
}
