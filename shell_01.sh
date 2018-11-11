#!/bin/bash

HONEYPOT_DIR='/root/work/honeypot'
MALWARE_DIR='/root/work/malware'
echo $HONEYPOT_DIR
echo $MALWARE_DIR

if [ ! -e $HONEYPOT_DIR/downloads.tar.gz ]
	then
		echo "Not Found File"
		exit 0
	else
		echo "Found File"
	fi

mv $HONEYPOT_DIR/downloads.tar.gz $MALWARE_DIR
gunzip -v /root/work/malware/downloads.tar.gz
tar -xvf /root/work/malware/downloads.tar -C /root/work/malware/

for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
do
gunzip -v /root/work/malware/downloads/downloads.tgz.$i.gz
# check exist folder
mkdir /root/work/malware/downloads/data$i
tar -xzvf /root/work/malware/downloads/downloads.tgz.$i -C /root/work/malware/downloads/data$i
done
