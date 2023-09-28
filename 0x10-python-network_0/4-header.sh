#!/bin/bash
# Send a get request with specified header data
curl -s "$1" -X GET -H "X-School-User-Id: 98"
