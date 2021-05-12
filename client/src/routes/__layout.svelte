<script>
  import '../app.postcss';

  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';

  import Sidebar from '$lib/components/Sidebar.svelte';

  import { isAuthorized } from '$lib/auth';

  let render = false;

  onMount(async () => {
    const success = await isAuthorized(window.location.pathname);

    if (!success) {
      await goto('/login');
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
