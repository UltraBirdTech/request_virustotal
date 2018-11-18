#!/bin/bash

MALWARE_DOWNLOAD_DIR='/root/work/malware/downloads'
MALWARE_DOWNLOAD_TAR='/root/work/malware/downloads.tar'

rm -rf $MALWARE_DOWNLOAD_DIR/data*
rm $MALWARE_DOWNLOAD_DIR/downloads.tgz.*
rm -rf $MALWARE_DOWNLOAD_DIR
rm $MALWARE_DOWNLOAD_TAR
