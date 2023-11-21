#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept.Send HEAD request, retrieve "Allow" header, and display the allowed methods
curl -sI "$1" | grep Allow | cut -d ' ' -f2-
