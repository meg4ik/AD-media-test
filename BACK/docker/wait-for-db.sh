#!/bin/sh
echo "Waiting for database..."

while ! nc -z $DB_HOST $DB_PORT; do
  sleep 0.1
done

echo "Database started"

exec "$@"
