#!/bin/bash

HONEYPOT_DIR='/root/work/honeypot'
MALWARE_DIR='/root/work/malware'
echo $HONEYPOT_DIR
echo $MALWARE_DIR
exit 0
# check file
mv /root/work/honeypot/downloads.tar.gz /root/work/malware/
gunzip -v /root/work/malware/downloads.tar.gz
tar -xvf /root/work/malware/downloads.tar -C /root/work/malware/

for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
do
gunzip -v /root/work/malware/downloads/downloads.tgz.$i.gz
# check exist folder
mkdir /root/work/malware/downloads/data$i
tar -xzvf /root/work/malware/downloads/downloads.tgz.$i -C /root/work/malware/downloads/data$i
done
