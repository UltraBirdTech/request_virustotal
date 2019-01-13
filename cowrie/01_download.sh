#!/bin/bash

HONEYPOT_DIR='./downloads'
PEM='/Users/hatoritakuya/.ssh/honeypot.pem'
PORT='64295'
HONEY_DOMAIN='honey@ec2-13-114-189-98.ap-northeast-1.compute.amazonaws.com'
HONEY_FILE_TAR='/home/honey/downloads.tar.gz'

scp -i $PEM -P $PORT $HONEY_DOMAIN:$HONEY_FILE_TAR $HONEYPOT_DIR
