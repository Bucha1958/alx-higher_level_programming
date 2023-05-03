#!/bin/bash
# Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond
curl -X PUT "http://0.0.0.0:5000/catch_me" -H "Content-Type: application/json" -d '{"message": "You got me!"}' -w "\n"
