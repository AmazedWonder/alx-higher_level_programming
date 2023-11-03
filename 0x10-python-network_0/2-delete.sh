#!/bin/bash
# script that sends a DELETE request to the URL passed as the first argument and displays the body of the response

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Error: URL argument is required."
    exit 1
fi

# Send DELETE request
curl -sX "DELETE" "$1"
