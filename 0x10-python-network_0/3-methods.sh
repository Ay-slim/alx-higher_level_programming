#!/bin/bash
# Display methods acceptable by the server
curl -sI "$1" -X OPTIONS| awk '/Allow/ {print substr($0, index($0, ":") + 2)}' | tr -d '\r'
