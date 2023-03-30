#!/bin/bash
# a script that takes in a URL,sends a request to that URL
curl -Is "$1" | grep "Content-Length" | cut -d ' ' -f 2
