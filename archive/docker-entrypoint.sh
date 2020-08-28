#!/bin/sh
set -e
# flask db upgrade
gunicorn --worker-class gevent --workers 4 --bind 0.0.0.0:5000 wsgi:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info
