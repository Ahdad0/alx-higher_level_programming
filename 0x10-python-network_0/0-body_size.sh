#!/usr/bin/env bash
# takes in a URL, sends a request to that URL

curl -Is "$1" | grep Content-Length | tr -d ' ' | cut -d":" -f2
