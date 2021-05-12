FROM mhart/alpine-node:16.0.0

# Change with `--build-arg VITE_API_URL=<url>` when building
ARG VITE_API_URL=http://127.0.0.1:5000

WORKDIR /app
COPY package.json package-lock.json svelte.config.js postcss.config.cjs tailwind.config.cjs ./
RUN npm i

COPY src ./src
COPY static ./src
RUN npm run build

EXPOSE 3000
CMD ["node", "build"]
