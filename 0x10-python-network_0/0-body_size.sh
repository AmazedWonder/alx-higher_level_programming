#!/bin/bash
# Bash script that takes in a URL, sends a request to that
# URL, and displays the size of the body of the response

# Check if URL argument is provided
#if [ -z "$1" ]; then
    #echo "Error: URL argument is required."
    #exit 1
#fi

# Send request and retrieve the size of the response body
#size=$(curl -w "%{size_download}\n" "$1" -so /dev/null)

# Display the size of the response body
#echo "$size"
curl -w "%{size_download}\n" "$1" -so /dev/null
