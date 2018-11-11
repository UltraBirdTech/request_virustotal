#!/bin/bash

MALWARE_DOWNLOAD_DIR='/root/work/malware/downloads'

for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
do
gunzip -v $MALWARE_DOWNLOAD_DIR/downloads.tgz.$i.gz
if [ ! -e $MALWARE_DOWNLOAD_DIR/data$i ]
  then
    echo 'create folder'
    mkdir $MALWARE_DOWNLOAD_DIR/data$i
  fi
tar -xzvf $MALWARE_DOWNLOAD_DIR/downloads.tgz.$i -C $MALWARE_DOWNLOAD_DIR/data$i
done
