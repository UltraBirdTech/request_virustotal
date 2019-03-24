#!/bin/bash

MALWARE_DOWNLOAD_DIR='./downloads'
HONEYPOT_DIR='home/honey/downloads'
DOWNLOAD_DIR='data/cowrie/downloads/*'

folder_num=$(ls $MALWARE_DOWNLOAD_DIR | grep data* | wc -l)

echo '[START]aggregnation shell.'
echo "folder num is $folder_num"
if [ ! -e "$MALWARE_DOWNLOAD_DIR/malware" ]
  then
    echo 'create new folder'
    mkdir $MALWARE_DOWNLOAD_DIR/malware
else
    echo 'delete previous files.'
#    rm $MALWARE_DOWNLOAD_DIR/malware/*
  fi

echo 'aggregation files.'
for i in `seq $folder_num`
do
  cp -p $MALWARE_DOWNLOAD_DIR/data$i/$DOWNLOAD_DIR $MALWARE_DOWNLOAD_DIR/malware
done

echo '[FINISH]aggregnation shell.'
