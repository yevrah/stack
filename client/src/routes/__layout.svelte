<script context="module">
  import { isAuthorized } from '$lib/auth';
  import { get } from 'svelte/store';
  import auth from '$lib/stores/auth';

  export const load = async ({ page, fetch, session, context }) => {
    const ath = get(auth);

    if (ath) {
      const success = await isAuthorized(page.path);
      return success ? {} : { status: 302, redirect: '/login' };
    } else {
      return { props: { render: false } };
    }
  };
</script>

<script>
  import '../app.postcss';

  import Sidebar from '$lib/components/Sidebar.svelte';

  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';

  export let render;

  onMount(async () => {
    const local = localStorage.getItem('auth_token');

    if (!$auth && local) {
      auth.set(local);
    }

    const success = await isAuthorized(window.location.pathname);

    if (!success) {
      goto('/login');
    } else {
      render = true;
    }
  });
</script>

{#if render}
  <Sidebar>
    <slot />
  </Sidebar>
{/if}
