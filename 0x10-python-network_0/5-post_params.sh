#!/bin/bash
# Send a post request with form data
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
