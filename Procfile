release: python manage.py migrate
web: bash -c "python manage.py createsuperuserauto || true && python manage.py collectstatic --noinput || true && gunicorn quizsite.wsgi --bind 0.0.0.0:${PORT:-8000} --workers 2 --timeout 120 --access-logfile - --error-logfile -"
