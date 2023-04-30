#!/bin/bash
# sends a request to a URL, and displays the size of the body of the response
response=$(curl -sS -w '%{size_download}' -o text.txt $1)
echo "$response"

