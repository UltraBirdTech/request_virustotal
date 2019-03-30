#!/bin/bash

OPERATE_DIONAEA_PATH='/home/honey/virustotal_api/dionaea'
MALWARE_DOWNLOAD_DIR='downloads'
OPERATE_PATH=$OPERATE_DIONAEA_PATH/$MALWARE_DOWNLOAD_DIR

echo '[START]delete file and direcotry'
rm $OPERATE_PATH/dionaea_malwares.tar
rm -rf $OPERATE_PATH/home
rm -rf $OPERATE_PATH/malware
rm -rf $OPERATE_PATH/data*
rm -rf $OPERATE_PATH/binaries*
echo '[FINISH]delete file and direcotry'
