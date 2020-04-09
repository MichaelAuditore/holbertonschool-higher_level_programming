#!/bin/bash
# Script to send a post request with params
curl -sP -G "$1" -d 'email=hr@holbertonschool.com' -d 'subject=I%20will%20always%20be%20here%20for%20PLD'
