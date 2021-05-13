# Client

## Requirements

- NodeJS >= v14.x

## Setup/Development

Install dependencies:

```
npm i
```

Add an `.env` file.

```
# All keys are prefixed with `VITE`.
# See: https://vitejs.dev/guide/env-and-mode.html

# Secret for cookie IDs. You must make your own one!!!
# For example, by using: `openssl rand -base64 32`
VITE_SECRET_KEY=<secret>

# API url
VITE_API_URL=http://127.0.0.1:5000
```

Start the development server:

```bash
npm run dev
```

## Important Libraries

- [SvelteKit](https://kit.svelte.dev)
- [Tailwind CSS](https://tailwindcss.com)
- [svelte-forms-lib](https://svelte-forms-lib-sapper-docs.vercel.app)
- [Axios](https://axios-http.com)
