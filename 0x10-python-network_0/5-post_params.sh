#!/bin/bash
# script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Error: URL argument is required."
    exit 1
fi

# Send POST request with form data and display the response body
response=$(curl -s -X POST -d "subject=I will always be here for PLD&email=test@gmail.com" "$1")
echo "$response"
