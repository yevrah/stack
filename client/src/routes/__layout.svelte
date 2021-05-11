<script context="module" lang="ts">
  import isAuthorized from '$lib/auth';

  export async function load({ page, fetch, session, context }) {
    return await isAuthorized({ page, fetch, session, context });
  }
</script>

<main>
  <slot />
</main>
