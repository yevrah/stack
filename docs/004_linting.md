# Code Linting and Formatting

Code linters and formatters are important for any codebase to keep a consistent and non-fugly quality of code.

Both `package.json` and `requirements_dev.txt` include the recommended (by me, a proper authority on non-fugly code) code linters/formatters to use in their respective projects. Their needed configuration files have also already been created. Here's a basic guide on how to use them once installed.

## Client

Our front-end uses [ESLint](https://eslint.org) for linting and [Prettier](https://prettier.io) for formatting. In `/client` you can run the following commands:

```bash
# Lint the project
npm run lint

# Format the project
npm run format
```

## Server

The back-end uses [Flake8](https://flake8.pycqa.org/en/latest/) for linting and [Black](https://github.com/psf/black) for formatting. In `/server` you can run the following commands:

```bash
# Lint the project
flake8 . --extend-exclude=env/ --show-source --statistics

# Format the project
black . --extend-exclude=env/
```

## Editor Integrations

Most of the time you don't want to constantly run lint and formatting commands, your editor should do that for you! Thankfully, all the linters/formatters that we're using are very common, so it should be pretty easy for you to find easy ways of integrating it into your editor of choice.

For example, if you use Neovim, you would want to install [coc.nvim](https://github.com/neoclide/coc.nvim). This is a [Language Server Protocol](https://en.wikipedia.org/wiki/Language_Server_Protocol) (LSP) client for Neovim, which allows you to connect to several language servers. I'm not going to explain it any more, go read the docs for it.

But to work with our project you want the following extensions:

- coc-eslint
- coc-prettier
- coc-pyright (you need to set the config to use Flake8 and Black)

And if you're feeling extra fancy:

- coc-tailwind (but you should probably use [my fork](https://github.com/beanpuppy/coc-tailwindcss) as it works with `.cjs` files)

Now Neovim will automatically lint your files when you are editing them and you can format them by using `:Format` or when the file is saved, depending on your preference.

For the other editors, here are basic some steps to set up a LSP client:

```bash
brew uninstall ${YOUR_EDITOR}
brew install neovim
```

Then do the instructions for Neovim! [Easy Breazy](https://www.youtube.com/watch?v=8-91y7BJ8QA)!

## GitHub Actions

The GitHub actions included lint the project and fail if they see something wrong, so make sure you format often! Otherwise your commit will get a big cross next to it and you'll be the laughing stock of your entire team.

I'll leave with a word of advice:

> No one will take you seriously any more (assuming they ever did) if you commit fugly code to the repo.
