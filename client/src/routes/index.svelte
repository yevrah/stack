<script>
  import { user } from '$lib/stores';
</script>

<svelte:head>
  <title>Les Fans D'Astolfo</title>
</svelte:head>

<div>
  <p class="text-4xl">Les Fans D'Astolfo</p>
  <p>You are logged in as: {$user.email}</p>
</div>
