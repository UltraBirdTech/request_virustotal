#!/bin/bash

MALWARE_DOWNLOAD_DIR='/root/work/malware/home'
MALWARE_DOWNLOAD_TAR='/root/work/malware/downloads.tar'

echo '[START]delete file and direcotry'
rm -rf $MALWARE_DOWNLOAD_DIR
rm $MALWARE_DOWNLOAD_TAR
echo '[FINISH]delete file and direcotry'
