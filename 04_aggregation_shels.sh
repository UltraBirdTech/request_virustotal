#!/bin/bash

MALWARE_DOWNLOAD_DIR='/root/work/malware'
HONEYPOT_DIR='home/honey/downloads'
DOWNLOAD_DIR='data/cowrie/downloads/*'

file_num=$(ls $MALWARE_DOWNLOAD_DIR/$HONEYPOT_DIR | grep data* | wc -l)

echo '[START]aggregnation shell.'
echo "file num is $file_num"
if [ ! -e "$MALWARE_DOWNLOAD_DIR/$HONEYPOT_DIR/malware" ]
  then
    mkdir $MALWARE_DOWNLOAD_DIR/$HONEYPOT_DIR/malware
else
    rm $MALWARE_DOWNLOAD_DIR/$HONEYPOT_DIR/malware/*
  fi

for i in `seq $file_num`
do
  cp -p $MALWARE_DOWNLOAD_DIR/$HONEYPOT_DIR/data$i/$DOWNLOAD_DIR $MALWARE_DOWNLOAD_DIR/$HONEYPOT_DIR/malware
done

echo '[FINISH]aggregnation shell.'
