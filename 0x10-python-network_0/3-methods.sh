#!/bin/bash
# sends a request and desplay all methods
curl -sI "$1" | grep "allow" | cut -d " " -f 2-
