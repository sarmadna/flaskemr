#! /usr/bin/bash

cd /data/flaskemr/
source venv/bin/activate
waitress-serve --host='127.0.0.1' --port=8080 flaskemr:app
