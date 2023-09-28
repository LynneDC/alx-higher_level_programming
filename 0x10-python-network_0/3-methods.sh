#!/bin/bash
# sends a request and desplay all methods
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
