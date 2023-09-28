#!/bin/bash
# Send post data from a json file
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
