#!/usr/bin/env bash
env_file_path="/home/tumn/app/.env"

echo "FLASK_APP=tumn/__init__.py" >> $env_file_path
echo "FLASK_DEBUG=false" >> $env_file_path

echo "===========ENV FILE==========="
cat $env_file_path
echo "=============================="
exec "$@"
