# Server

## Requirements

* Python 3.7+
* PostgreSQL 11+
* Redis 6.2+

## Setup/Development

Install requirements:

```bash
pip install -r requirements_dev.txt
```

Add an `.env` file for API keys or database connection settings. For example:

```
# See config.py for all variables
DB_USER=<user>
DB_PASSWORD=<password>
```

Run migrations:

```bash
rider migrate
```

Start the server:

```
python3 app.py
```
