#!/bin/bash
# Display size of response body
curl -sI "$1" | awk '/Content-Length/ {print $2}' | tr -d '\r'
