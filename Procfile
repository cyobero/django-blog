web: gunicorn blog.wsgi --log-file -
python manage.py collectstatic --noinput
manage.py migrate
