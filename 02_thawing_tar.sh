#!/bin/bash

HONEYPOT_DIR='./downloads'
DOWNLOAD_DIR='./downloads'
MALWARE_DIR='/root/work/malware'
DOWNLOAD_FILE='downloads.tar.gz'
TAR_FILE='downloads.tar'

echo 'start move a tar file from /root/work/honeypot to /root/work/malware'
if [ ! -e $DOWNLOAD_DIR/downloads.tar.gz ]
  then
    echo "Not Found File. Please check $DOWNLOAD_DIR/$DOWNLOAD_FILE"
else
#    mv $HONEYPOT_DIR/$DOWNLOAD_FILE $MALWARE_DIR
    echo 'test'
  fi
echo 'move a tar file is finishe.'

######## gunzip tar file #############
echo 'gunzip tar file'
#gunzip -v $MALWARE_DIR/$DOWNLOAD_FILE
gunzip -v $DOWNLOAD_DIR/$DOWNLOAD_FILE
echo 'gunzip is finish'

######## thawing tar file #############
echo 'tar thawing is start'
tar -xvf $DOWNLOAD_DIR/$TAR_FILE -C $DOWNLOAD_DIR
echo 'tar thawing is finished.'
