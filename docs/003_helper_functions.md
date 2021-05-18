# Commonly Used Helper Functions

This document outlines the most used helper functions/modules through out the stack.

## Client

- `ax` from `$lib/axios`.

This is `axios` instance that has the `VITE_API_URL` set as its' base and deals with automatically refreshing the users' access token if it has expired. This should always be used unless you want to make an unauthenticated request or make a request to a different domain.

Example usage:

```javascript
import ax from '$lib/axios';

let res = await ax.get('/auth/me');
```

## Server

- `insert_eh`/`update_eh` from `src.schemas.base.BaseSchema`.

These are schema functions to handle errors in the correct fashion (returning a tuple instead of raising an error) and should always be used instead of the normal `insert`/`update`.

They also make you Canadian ("eh" stands for "error handle").

Example usage:

```python
user, error = User.insert(data)

if error is not None:
  return error, 400

return user, 200
```

- `get_by_id` from `src.schemas.base.BaseSchema`.

Gets a row by its' `id` and returns `None` if it doesn't exist.

Example usage:

```python
user = User.get_by_id(1337)

if user is None:
  return {"error": "not found"}, 404

return user, 200
```
