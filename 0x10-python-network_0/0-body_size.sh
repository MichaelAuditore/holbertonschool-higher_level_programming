#!/bin/bash
# Script to displays the size of the body of the response sent to an URL
curl -s "$1" | wc -c
