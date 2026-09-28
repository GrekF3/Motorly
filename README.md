# Motorly

A compact Django catalog for managing and browsing vehicle listings.

## Run locally

```bash
cd ShopCar
python -m venv .venv
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Database and Django credentials are configured through environment variables.
