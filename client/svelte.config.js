import adapter from '@sveltejs/adapter-node';
import preprocess from 'svelte-preprocess';
/** @type {import('@sveltejs/kit').Config} */
const config = {
  preprocess: [
    preprocess({
      postcss: true
    })
  ],
  kit: {
    target: '#svelte',
    adapter: adapter({ out: 'build' })
  }
};

export default config;
