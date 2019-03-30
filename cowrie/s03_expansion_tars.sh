#!/bin/bash

CURRENT_PATH='/home/honey/virustotal_api/cowrie'
MALWARE_DOWNLOAD_DIR='downloads'
OPERATE_PATH=$CURRENT_PATH/$MALWARE_DOWNLOAD_DIR

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

echo '---------------------------'
echo $OPERATE_PATH

for i in `seq $num`
do
gunzip -v $OPERATE_PATH/downloads.tgz.$i.gz
if [ ! -e $OPERATE_PATH/data$i ]
  then
    echo 'create folder'
    mkdir $OPERATE_PATH/data$i
fi
tar -xzvf $OPERATE_PATH/downloads.tgz.$i -C $OPERATE_PATH/data$i
done

echo 'finish expansiton tars'
