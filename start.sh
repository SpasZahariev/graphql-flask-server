#!/bin/bash

cd /src

#only works on heroku since it sets a PORT as an environment variable that I MUST work with
gunicorn --bind 0.0.0.0:${PORT} main:app

#use this for windows
# gunicorn --bind 0.0.0.0:5000 main:app