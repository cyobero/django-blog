web: gunicorn blog.wsgi --log-file -
python manage.py collectstatic --noinput
python manage.py migrate
