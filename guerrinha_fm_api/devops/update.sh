#!/bin/bash

set -e  # exit if any command fails

echo "🛠️ Applying migrations..."
python manage.py migrate

echo "🌱 Running seeds..."
python manage.py seed

echo "⏱️ Fetching missing durations..."
python manage.py fetch_durations

echo "✅ Done!"
