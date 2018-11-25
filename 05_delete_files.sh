#!/bin/bash

MALWARE_DOWNLOAD_DIR='/root/work/malware/home/honey'
MALWARE_DOWNLOAD_TAR='/root/work/malware/downloads.tar'

echo '[START]delete file and direcotry'
rm -rf $MALWARE_DOWNLOAD_DIR/data*
rm $MALWARE_DOWNLOAD_DIR/downloads.tgz.*
rm -rf $MALWARE_DOWNLOAD_DIR
rm $MALWARE_DOWNLOAD_TAR
echo '[FINISH]delete file and direcotry'
