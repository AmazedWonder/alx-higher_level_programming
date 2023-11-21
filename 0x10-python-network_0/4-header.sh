#!/bin/bash
# cript that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response.Send GET request with custom header and display the response body
curl -s -H "X-School-User-Id:98" "$1"
