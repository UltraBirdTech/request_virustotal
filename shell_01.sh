#!/bin/bash

HONEYPOT_DIR='/root/work/honeypot'
MALWARE_DIR='/root/work/malware'
DOWNLOAD_FILE='downloads.tar.gz'
TAR_FILE='downloads.tar'

if [ ! -e $HONEYPOT_DIR/downloads.tar.gz ]
  then
    echo "Not Found File. Please check $HONEYPOT_DIR/downloads.tar.gz"
    exit 0
  fi

mv $HONEYPOT_DIR/downloads.tar.gz $MALWARE_DIR
gunzip -v $MALWARE_DIR/downloads.tar.gz
tar -xvf $MALWARE_DIR/downloads.tar -C $MALWARE_DIR
