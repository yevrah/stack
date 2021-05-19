# Commonly Used Helper Functions

This document outlines the most used helper functions/modules throughout the stack.

## Client

- `ax` from `$lib/axios`.

This is an `axios` instance that has the `VITE_API_URL` set as its base and deals with automatically refreshing the users' access token if it has expired. This should always be used instead of the default `axios` unless you want to make an unauthenticated request or make a request to a different domain.

Example usage:

```javascript
import ax from '$lib/axios';

let res = await ax.get('/auth/me');
```

## Server

- `insert_eh`/`update_eh` from `src.schemas.base.BaseSchema`.

These are schema functions to handle a `FieldError` in the correct fashion (returning a tuple instead of raising an error) and should always be used instead of the normal `insert`/`update`. The error returned is the first argument from the exception raised.

**Only** `FieldError` will be handled, all other errors will still raise, so it's mainly used for validation. You can read about validation in Estoult [here](https://estoult.readthedocs.io/en/latest/how_tos.html#validation).

The functions are also from Canada ("eh" stands for "error handle").

Example usage:

```python
user, error = User.insert_eh(data)

if error is not None:
    return error, 400

return user, 200
```

- `db.atomic` from `src.schemas.base.db`.

This is actually from the normal Estoult `Database` object, but it's important enough to put here. It runs an entire block as a transaction in the database. You should put this on **every** route that updates or inserts (along with using the Canada functions).

Example usage (as a decorator):

```python
import db from src.schemas.base.db

@bl.post("/register")
@db.atomic()
def register():
    # Do your stuff here
    pass
```

Example usage (as a runtime context):

```python
import db from src.schemas.base.db

with db.atomic():
    # Do your stuff here
    pass
```

- `get_by_id` from `src.schemas.base.BaseSchema`.

Gets a row by its `id` and returns `None` if it doesn't exist.

Example usage:

```python
user = User.get_by_id(1337)

if user is None:
    return {"error": "not found"}, 404

return user, 200
```
