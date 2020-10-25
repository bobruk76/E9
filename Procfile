release: alembic upgrade head
release: python manage.py loaddata fixtures.json
web: gunicorn -w 4 -b 0.0.0.0:5000 api:app
