#!/bin/bash

# This is just an example script to use for walking through the RPM
# build process.

source /usr/local/etc/local-ports.conf

/bin/nmap `/sbin/ip route get 1.1.1.1 | /bin/grep -oP 'src \K\S+'` >> ${logdir}/${logfile}
