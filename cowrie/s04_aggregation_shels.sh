#!/bin/bash

CURRENT_PATH='/home/honey/virustotal_api/cowrie'
MALWARE_DOWNLOAD_DIR='downloads'
OPERATE_PATH=$CURRENT_PATH/$MALWARE_DOWNLOAD_DIR

HONEYPOT_DIR='home/honey/downloads'
DOWNLOAD_DIR='data/cowrie/downloads/*'

folder_num=$(ls $OPERATE_PATH | grep data* | wc -l)

echo '[START]aggregnation shell.'
echo "folder num is $folder_num"
if [ ! -e "$OPERATE_PATH/malware" ]
  then
    echo 'create new folder'
    mkdir $OPERATE_PATH/malware
else
    echo 'delete previous files.'
#    rm $MALWARE_DOWNLOAD_DIR/malware/*
  fi

echo 'aggregation files.'
for i in `seq $folder_num`
do
  cp -p $OPERATE_PATH/data$i/$DOWNLOAD_DIR $OPERATE_PATH/malware
done

echo '[FINISH]aggregnation shell.'
