#!/bin/bash
# Display status code only
curl -I -s -o /dev/null -w "%{http_code}" "$1"
