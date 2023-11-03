#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept.

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Error: URL argument is required."
    exit 1
fi

# Send HEAD request, retrieve "Allow" header, and display the allowed methods
allowed_methods=$(curl -sI "$1" | grep Allow | cut -d ' ' -f2-)
echo "$allowed_methods"
