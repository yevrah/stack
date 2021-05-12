<script context="module">
  import { isAuthorized } from '$lib/auth';
  import { get } from 'svelte/store';
  import auth from '$lib/stores/auth';

  export const load = async ({ page, fetch, session, context }) => {
    const ath = get(auth);

    if (ath) {
      const [aut, success] = await isAuthorized(page.path);
      return success ? { props: aut } : aut;
    } else {
      return { props: { render: false, page } };
    }
  };
</script>

<script>
  import '../app.postcss';
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';

  export let render;
  export let page;

  onMount(async () => {
    const ath = get(auth);
    const local = localStorage.getItem("auth_token");

    if (!ath && local) {
      auth.set(local);
    }

    const [_, success] = await isAuthorized(window.location.pathname);

    if (!success) {
      goto('/login');
    } else {
      render = true;
    }
  });
</script>

{#if render}
  <main>
    <slot />
  </main>
{/if}
