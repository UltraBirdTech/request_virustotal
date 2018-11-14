#!/bin/bash

MALWARE_DOWNLOAD_DIR='/root/work/malware/downloads'

echo ls $MALWARE_DOWNLOAD_DIR

file_num=$(ls $MALWARE_DOWNLOAD_DIR | grep data* | wc -l)

echo $file_num

for i in `seq $file_num`
do
	echo $i
done
