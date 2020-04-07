#!/bin/bash
# send a POST request with a JSON
curl -H "Content-Type: application/json" -X POST -d "@$2" "$1"
