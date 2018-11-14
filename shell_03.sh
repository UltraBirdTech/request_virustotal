#!/bin/bash

MALWARE_DOWNLOAD_DIR='/root/work/malware/downloads'

file_num=$(ls $MALWARE_DOWNLOAD_DIR | grep data* | wc -l)

echo $file_num

if [ ! -e "$MALWARE_DOWNLOAD_DIR/malware" ]
  then
    mkdir $MALWARE_DOWNLOAD_DIR/malware
  fi

for i in `seq $file_num`
do
  cp $MALWARE_DOWNLOAD_DIR/data$i/data/cowrie/downloads/* $MALWARE_DOWNLOAD_DIR/malware
done
