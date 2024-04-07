#!/bin/sh
TRAFFFIC=$1

if [ "$TRAFFFIC" = "rtm" ]; then
    echo "Titans rtm data api batch started "
elif [ "$TRAFFFIC" = "rtti" ]; then
    echo "Titans rtti data api batch started "
elif [ "$TRAFFFIC" = "pattern" ]; then
    echo " Titans pattern data api batch started "
else
    echo "Invalid traffic type. Please provide valid traffic type."
fi

