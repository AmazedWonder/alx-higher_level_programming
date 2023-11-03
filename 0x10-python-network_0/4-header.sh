#!/bin/bash
# cript that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Error: URL argument is required."
    exit 1
fi

# Send GET request with custom header and display the response body
response=$(curl -s -H "X-School-User-Id:98" "$1")
echo "$response"
