<script context="module">
  import { isAuthorized } from '$lib/auth';
  import { refresh } from '$lib/stores/auth';

  export const load = async ({ session, page }) => {
    refresh.set(session.refresh_token);
    const success = await isAuthorized(page.path);
    return success ? {} : { status: 302, redirect: '/login' };
  };
</script>

<script>
  import '../app.postcss';

  import Sidebar from '$lib/components/Sidebar.svelte';
</script>

<Sidebar>
  <slot />
</Sidebar>
