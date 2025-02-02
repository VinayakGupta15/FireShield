#!/bin/bash

# Simulate port scanning using nmap
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <target_ip>"
    exit 1
fi

target_ip=$1
nmap -Pn $target_ip