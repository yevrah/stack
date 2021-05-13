import { writable } from 'svelte/store';

const auth = writable('');
const refresh = writable('');

export { auth, refresh };
