#!/bin/bash

DIONAEA_OPERATE_PATH='/home/honey/virustotal_api/dionaea'
MALWARE_DOWNLOAD_DIR='downloads'
OPERATE_PATH=$DIONAEA_OPERATE_PATH/$MALWARE_DOWNLOAD_DIR

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
gunzip -v $OPERATE_PATH/binaries.tgz.$i.gz
if [ ! -e $OPERATE_PATH/data$i ]
  then
    echo 'create folder'
    mkdir $OPERATE_PATH/data$i
fi
tar -xzvf $OPERATE_PATH/binaries.tgz.$i -C $OPERATE_PATH/data$i
done

echo 'finish expansiton tars'
