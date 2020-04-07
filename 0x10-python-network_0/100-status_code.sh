#!/bin/bash
# Script to get the status code of a request
curl -s -o /dev/null -w "%{http_code}" "$1"
