<script>
  import { user } from '$lib/stores';
</script>

<svelte:head>
  <title>Profile</title>
</svelte:head>

<div>
  <p class="text-4xl">Profile Page</p>
  <p>You are logged in as: {$user.email}</p>
</div>
