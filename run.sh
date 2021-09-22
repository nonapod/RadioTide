#!/bin/sh
PYTHON=$(which python | awk '{print $1}')
$PYTHON ./radtide.py
