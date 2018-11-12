#!/bin/bash

MALWARE_DOWNLOAD_DIR='/root/work/malware/downloads'

echo $#
echo $1
num=$1
echo "First: $num"
if [ ! -n "$num" ]
  then
    num='7'
  fi

echo "Second: $num"

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
