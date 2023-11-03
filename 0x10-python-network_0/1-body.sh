#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
#curl -sL "$1"

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Error: URL argument is required."
    exit 1
fi

# Send GET request and display the response body
curl -sL "$1"
