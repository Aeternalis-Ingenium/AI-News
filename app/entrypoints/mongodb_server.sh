#!/bin/bash

echo "MongoDB Server --- Connecting . . ."

while ! nc -z mongodbServer 27017; do

    echo "MongoDB Server -- Failed!"

    sleep 1

    echo "MongoDB Server -- Reconnecting . . ."

done

echo "MongoDB Server --- Successfully Connected!"

exec "$@"
