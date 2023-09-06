#!/bin/bash

set -e

# Check for ENV existence
vars=("PROJECT_STAGE" "POSTGRES_DB_HOST")
errors=()
for t in ${vars[@]}; do
  eval "if [[ -z \$"$t" ]]; then  errors+=( $t ); fi"
done

if [ -n "$errors" ]; then
    echo "Missing ENV:"
    echo ${errors[@]}
    exit 1
fi

# Wait for database
until pg_isready -h "${POSTGRES_DB_HOST}"
do
  echo "Waiting for PostgreSQL ${POSTGRES_DB_HOST}";
  sleep 1;
done

# Start!
if [ "$START_MODE" == "BACKEND" ]; then
  # Database migrations
  python $APP_DIR/manage.py migrate
  python $APP_DIR/manage.py collectstatic -v 0 --no-input --clear
  # Run service
  if [ "$PROJECT_STAGE" == "local" ]; then
    python $APP_DIR/manage.py runserver 0.0.0.0:8000
  else
    gunicorn -c $APP_DIR/conf/gunicorn-wsgi.conf.py
  fi
else
  echo "Unknown START_MODE!";
  exit 1;
fi

exec "$@"
