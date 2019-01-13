#!/bin/bash

DOWNLOAD_DIR='./downloads'
DOWNLOAD_FILE='dionaea_malwares.tar.gz'
TAR_FILE='dionaea_malwares.tar'

if [ ! -e $DOWNLOAD_DIR/dionaea_malwares.tar.gz ]
  then
    echo "Not Found File. Please check $DOWNLOAD_DIR/$DOWNLOAD_FILE"
    exit 0
else
    echo 'Found File'
  fi
echo 'move a tar file is finishe.'

######## gunzip tar file #############
echo 'gunzip tar file'
gunzip -v $DOWNLOAD_DIR/$DOWNLOAD_FILE
echo 'gunzip is finish'

######## thawing tar file #############
echo 'tar thawing is start'
tar -xvf $DOWNLOAD_DIR/$TAR_FILE -C $DOWNLOAD_DIR
echo 'tar thawing is finished.'
