#/bin/sh

EXPOSE_PORT=8000

until wget db:3306; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 2
done

python3 manage.py runserver 0.0.0.0:${EXPOSE_PORT}