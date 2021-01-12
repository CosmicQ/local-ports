#!/bin/bash

# This is just an example script to use for walking through the RPM
# build process.

source /usr/local/etc/local-ports.conf

nmap `ip route get 1.1.1.1 | grep -oP 'src \K\S+'` >> ${logdir}/${logfile}
