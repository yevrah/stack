# Sessions

Before we get started you should probably know what JSON Web Tokens are. You can click [here](https://jwt.io) to learn about them.

> Session management took me at least 4 hours to completely think through and implement, so you better appreciate it.

Back? Here are the acronyms that we will be using:

- **JSON Web Token:** JWT
- **SvelteKit Server:** SKS
- **SvelteKit Application:** SKA
- **Flask Server:** FS

Now let's go through the login process. I'll explain it after.

1. The user types in their login credentials and submits them.
2. SKA submits the credentials to SKS (`/login`).
3. SKS proxies the credentials to FS (`/auth/token`).
4. FS verifies login credentials.
5. FS creates a JWT (if login credentials are correct, otherwise it returns an error).
6. FS returns an auth token and a refresh token back to SKS.
7. SKS creates a cookie with the refresh token.
8. SKS returns the auth back to SKA.
9. SKA redirects the user to the home page.

Having a front-end server that renders the application on the server side makes session management a _little_ more complicated than your usual application. Especially in our case, where our API server is in a different language and isn't what is serving SKA.

I think it would be better to explain why if we had an example not using SKS as a proxy and pretended this was your normal application.

1. The user types in their login credentials and submits them.
2. SKA submits the credentials to FS (`/auth/token`).
4. FS verifies login credentials.
5. FS creates a JWT (if login credentials are correct, otherwise it returns an error).
6. FS creates a cookie for SKA to use.
7. FS returns an auth token and a refresh token back to SKS.
8. SKA redirects the user to the home page.

Simpler right? Well kind of, but it also won't work at all.

SKA/SKS and FS are on different domains (they have to be), and unfortunately (or fortunately for the Internet in general), most browsers block third party cookies, so the cookie FS sets for us will never be accepted by the browser.

Okay then, if FS can't set a cookie for us, how about we just store the tokens in browser storage and manually get them when we make requests to the FS?

**NO!** That's an awful idea, why were you even thinking of that? Honestly, some people...

Cookies are already pretty poor in terms of security, but browser local/session stores are even worse! It's much easier to steal data from them via XSS/CSRF attacks.

We also want our sessions to be authorized **during** the server-side rendering process and not **after**. That is, we should check if the user is able to visit a page while SKS is rendering the page instead of after it has been sent to the user and the HTML DOM has been mounted. And since local/session storage only exists on the user's browser, we have no way of getting the tokens during the rendering process.

So, our only real option is to use cookies that are sent to SKS instead of FS. Now when a user requests the page from SKS:

1. The user's browser sends its cookies to SKS with the request.
2. SKS decrypts the cookie, getting a refresh token.
3. SKS gets an access token from FS using the refresh token.
3. SKS checks if the user is authorized.
3. SKS renders SKA and servers it to the user.

## A note on Redis and JWTs

You may have noticed that we use Redis for checking sessions, even though we use JWTs which are supposed to be stateless. This is again, for more security. JWTs aren't actually any better for user\* session management, as they have no methods of being revoked other then just expiring.

Without Redis, if a user logged out of the website, the cookie would be gone from the user's browser but the access/refresh would still be valid. And if someone were to have these tokens, they would still be able to use them. So, we use Redis to keep track of tokens that have been blacklisted (after the user logs out).

So why are we even using JWTs if their most prominent benefit is unused? I like them, and they're used a lot so it was easy to find libraries to do the hard work for us.

\* For client session management, JWTs are much more useful because you don't expect API clients to be storing tokens in something as insecure as cookies (because they shouldn't be storing them at all), so having the client just get rid of the token is probably enough.
