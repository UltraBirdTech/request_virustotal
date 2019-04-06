#!/bin/bash

COWRIE_OPERATE_PATH='/home/honey/virustotal_api/cowrie'
MALWARE_DOWNLOAD_DIR='downloads'
OPERATE_PATH=$COWRIE_OPERATE_PATH/$MALWARE_DOWNLOAD_DIR

echo '[START]delete file and direcotry'
rm $OPERATE_PATH/downloads.tar
rm -rf $OPERATE_PATH/home
rm -rf $OPERATE_PATH/malware
rm -rf $OPERATE_PATH/data*
rm -rf $OPERATE_PATH/downloads*
rm /home/honey/virustotal_api/cowrie_*
echo '[FINISH]delete file and direcotry'
