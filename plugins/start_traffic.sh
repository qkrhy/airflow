#!/bin/sh
FRUIT = $1

if [ "$FRUIT" = "prod" ]; then
    nohup python3 main.py --env=prod 1>/prod/null 2>&1 &
elif [ "$FRUIT" = "stg" ]; then
    nohup python3 main.py --env=stg 1>/stg/null 2>&1 &
else
    nohup python3 main.py --env=dev 1>/dev/null 2>&1 &
fi

