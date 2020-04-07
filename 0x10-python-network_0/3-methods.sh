#!/bin/bash
# Script to all available methods request
curl -sI "$1" | grep Allow | cut -d" " -f2-
