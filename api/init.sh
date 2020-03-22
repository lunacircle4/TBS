#!/bin/sh

until wget db:3306  -O /dev/null; do
  >&2 echo "mysql is unavailable - sleeping"
  sleep 3
done

python3 manage.py makemigrations
python3 manage.py migrate
