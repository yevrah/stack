FROM mhart/alpine-node:16.0.0

# Change with `--build-arg VITE_API_URL=<url>` when building
ARG VITE_API_URL=http://host.docker.internal:5000
ARG VITE_SECRET_KEY=7c147ee595e49aef6febd277ed36eb2ad3535c7ecd6f818f6da34b7093f1ded4

WORKDIR /app
COPY package.json package-lock.json svelte.config.js postcss.config.cjs tailwind.config.cjs ./
RUN npm i

COPY src ./src
COPY static ./src
RUN npm run build

EXPOSE 3000
CMD ["node", "build"]
