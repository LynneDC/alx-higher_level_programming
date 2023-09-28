#!/bin/bash
# sends a JSON POST request to a URL 
curl -s -H "Content-Type: Application/json" -d "$(cat "$2")" "$1"
