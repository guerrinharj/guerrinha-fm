#!/bin/bash

set -e  # exit on first error

echo "🛠️ Applying migrations..."
python manage.py makemigrations
python manage.py migrate

echo "🌱 Running seeds..."
python manage.py seed

echo "⏱️ Fetching missing durations..."
python manage.py fetch_durations

echo "✅ All done!"
