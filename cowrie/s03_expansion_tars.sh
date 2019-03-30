#!/bin/bash

CURRENT_PATH = '/homey/honey/virustotal_api/cowrie'
MALWARE_DOWNLOAD_DIR='./downloads'
HONEY_POT_DIR='home/honey/downloads'

echo 'start expansion tars'
num=$1
if [ ! -n "$num" ]
  then
    echo 'expansion tar file is 7 files'
    num='7'
elif [ $num -gt 15 ]
  then
    echo 'Option: Please input less 15.'
    exit 0
else
  echo "expansion tar file is $num files."
fi

for i in `seq $num`
do
gunzip -v $MALWARE_DOWNLOAD_DIR/downloads.tgz.$i.gz
if [ ! -e $MALWARE_DOWNLOAD_DIR/data$i ]
  then
    echo 'create folder'
    mkdir $MALWARE_DOWNLOAD_DIR/data$i
fi
tar -xzvf $MALWARE_DOWNLOAD_DIR/downloads.tgz.$i -C $MALWARE_DOWNLOAD_DIR/data$i
done

echo 'finish expansiton tars'
