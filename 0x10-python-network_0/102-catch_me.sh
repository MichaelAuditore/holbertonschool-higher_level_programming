#!/bin/bash
# Script to get a catch me from url 0.0.0.0:5000/catch_me
curl -s -L 0.0.0.0:5000/catch_me -X PUT -d "user_id=98" -H "Origin:HolbertonSchool"
