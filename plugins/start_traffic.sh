TRAFFFIC = $1

if [ "$TRAFFFIC" = "rtm" ]; then
    echo "Starting traffic for rtm"
elif [ "$TRAFFFIC" = "rtti" ]; then
    echo "Starting traffic for rtti"
elif [ "$TRAFFFIC" = "pattern" ]; then
    echo "Starting traffic for pattern"
else
    echo "Invalid traffic type. Please provide valid traffic type."
fi

