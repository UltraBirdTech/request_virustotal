#!/bin/bash

MALWARE_DOWNLOAD_DIR='/root/work/malware/downloads'


echo ls $MALWARE_DOWNLOAD_DIR

file_num=$(ls $MALWARE_DOWNLOAD_DIR | grep data* | wc -l)

echo $file_num

if [ ! -e "$MALWARE_DOWNLOAD_DIR/data" ]
  then
    mkdir $MALWARE_DOWNLOAD_DIR/data
  fi

for i in `seq $file_num`
do
	echo $MALWARE_DOWNLOAD_DIR
	echo $MALWARE_DOWNLOAD_DIR/data$i/data/cowrie/downloads
	echo $i
	
done
