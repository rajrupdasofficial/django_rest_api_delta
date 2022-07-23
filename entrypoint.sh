#!/bin/bash
cd /app/

/opt/env/bin/gunicorn --worker-tmp-dir /dev/shm tutorial.wsgi:application --bind "0.0.0.0:8000"
