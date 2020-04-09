#!/bin/bash
# send a POST request with a JSON
curl -H "Content-Type: application/json" -sX POST -d "@$2" "$1"
