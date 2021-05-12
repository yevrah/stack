<script>
  import { createForm } from 'svelte-forms-lib';
  import { goto } from '$app/navigation';

  import ax from '$lib/axios';
  import { user } from '$lib/stores';
  import auth from '$lib/stores/auth';

  let error = '';

  const { form, handleChange, handleSubmit } = createForm({
    initialValues: {
      email: '',
      password: ''
    },
    onSubmit: async (values) => {
      error = '';

      try {
        const res = await ax.post('/auth/login', values);

        user.set(res.data.user);
        auth.set(res.data.auth_token);
        localStorage.setItem('auth_token', res.data.auth_token);

        goto('/');
      } catch (e) {
        const err = e.response.data;
        error = err.msg;
      }
    }
  });
</script>

<div class="flex flex-col items-center justify-center w-screen h-screen min-h-full bg-gray-200">
  <div class="flex flex-col items-center w-1/4">
    <p class="mb-2 text-2xl">Login</p>

    <form on:submit={handleSubmit} class="flex flex-col items-center w-60">
      <input type="email" placeholder="Email" bind:value={$form.email} on:change={handleChange} />
      <input
        type="password"
        placeholder="Password"
        bind:value={$form.password}
        on:change={handleChange}
      />
      <button class="w-full p-2 text-gray-100 bg-gray-800">Submit</button>
      {#if error}
        <p class="mt-2 text-xs text-red-800">{error}</p>
      {/if}
      <div class="flex justify-center w-full mt-2 border border-black border-solid">
        <a class="p-2 text-sm text-blue-600" href="/register">New? Register Here</a>
      </div>
    </form>
  </div>
</div>

<style>
  input {
    @apply mb-2 p-2 text-sm w-full;
  }
</style>
