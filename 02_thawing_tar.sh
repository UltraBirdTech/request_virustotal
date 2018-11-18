#!/bin/bash

HONEYPOT_DIR='/root/work/honeypot'
MALWARE_DIR='/root/work/malware'
DOWNLOAD_FILE='downloads.tar.gz'
TAR_FILE='downloads.tar'

if [ ! -e $HONEYPOT_DIR/downloads.tar.gz ]
  then
    echo "Not Found File. Please check $HONEYPOT_DIR/$DOWNLOAD_FILE"
else
    mv $HONEYPOT_DIR/$DOWNLOAD_FILE $MALWARE_DIR
  fi

gunzip -v $MALWARE_DIR/$DOWNLOAD_FILE
tar -xvf $MALWARE_DIR/$TAR_FILE -C $MALWARE_DIR
