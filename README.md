# National Cancer Registry

Django 5.2 backend scaffold with the `config` project and `registry` application.
Development uses SQLite; production PostgreSQL configuration will be added when
preparing deployment. No patient models or registry workflows are implemented yet.

## Development

Requires Python 3.10 or newer (validated with Python 3.12).

```sh
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python manage.py migrate
.venv/bin/python manage.py check
.venv/bin/python manage.py runserver 0.0.0.0:8000
```

The root endpoint returns the service name and status as JSON. Django admin is
available at `/admin/`. To create a local admin account, run:

```sh
.venv/bin/python manage.py createsuperuser
```

SQLite data is stored in ignored `db.sqlite3`. The settings are for local
development. Production deployment requires PostgreSQL and its driver,
a private environment-provided secret key, `DEBUG=False`, explicit allowed hosts,
and deployment security settings.
