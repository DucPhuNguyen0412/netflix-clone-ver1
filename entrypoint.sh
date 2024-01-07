#!/bin/bash

# Wait for the database to be ready
# Add logic to wait for DB here

# Run populate_movies.py to populate the database
echo "Populating the database with movies..."
python /code/populate_movies.py

# Start the Django app
echo "Starting Django application..."
exec gunicorn netflix_site.wsgi:application --bind 0.0.0.0:8000
