#!/bin/bash

DIONAEA_OPERATE_PATH='/home/honey/virustotal_api/dionaea'
MALWARE_DOWNLOAD_DIR='downloads'
DOWNLOAD_DIR='data/dionaea/binaries/*'
OPERATE_PATH=$DIONAEA_OPERATE_PATH/$MALWARE_DOWNLOAD_DIR

folder_num=$(ls $OPERATE_PATH | grep data* | wc -l)

echo '[START]aggregnation shell.'
echo "folder num is $folder_num"
if [ ! -e "$OPERATE_{ATH/malware" ]
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
