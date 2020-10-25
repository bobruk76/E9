release: alembic upgrade head
web: gunicorn -w 4 -b localhost:5000 api:app --preload
