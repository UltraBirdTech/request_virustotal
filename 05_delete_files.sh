#!/bin/bash

MALWARE_DOWNLOAD_DIR='./downloads'

echo '[START]delete file and direcotry'
rm $MALWARE_DOWNLOAD_DIR/downloads.tar
rm -rf $MALWARE_DOWNLOAD_DIR/home
echo '[FINISH]delete file and direcotry'
