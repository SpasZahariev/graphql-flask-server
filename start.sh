#!/bin/bash

cd src

OPEN_PORT=${PORT}

if [$OPEN_PORT -e ''];then 
    OPEN_PORT='5000'
fi


gunicorn --bind 0.0.0.0:$OPEN_PORT main:app

#use this for windows
# gunicorn --bind 0.0.0.0:5000 main:app