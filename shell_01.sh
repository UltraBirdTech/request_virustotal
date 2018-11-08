#!/bin/sh

clear
#ls -la /root/work/malware/downloads

for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
do
echo $i
echo "/root/work/malware/downloads/donloads/tgz.$i.gz"
done
exit 0

cd /root/work/malware/downloads
gunzip -v /root/work/malware/downloads/downloads.tgz.1.gz
gunzip -v /root/work/malware/downloads/downloads.tgz.2.gz
gunzip -v /root/work/malware/downloads/downloads.tgz.3.gz
gunzip -v /root/work/malware/downloads/downloads.tgz.4.gz
gunzip -v /root/work/malware/downloads/downloads.tgz.5.gz
gunzip -v /root/work/malware/downloads/downloads.tgz.6.gz
gunzip -v /root/work/malware/downloads/downloads.tgz.7.gz
gunzip -v /root/work/malware/downloads/downloads.tgz.8.gz
gunzip -v /root/work/malware/downloads/downloads.tgz.9.gz
gunzip -v /root/work/malware/downloads/downloads.tgz.10.gz
gunzip -v /root/work/malware/downloads/downloads.tgz.11.gz
gunzip -v /root/work/malware/downloads/downloads.tgz.12.gz
gunzip -v /root/work/malware/downloads/downloads.tgz.13.gz
gunzip -v /root/work/malware/downloads/downloads.tgz.14.gz
gunzip -v /root/work/malware/downloads/downloads.tgz.15.gz

# check folders
tar -xzvf downloads.tgz.1 -C ./data1
tar -xzvf downloads.tgz.2 -C ./data2
tar -xzvf downloads.tgz.3 -C ./data3
tar -xzvf downloads.tgz.4 -C ./data4
tar -xzvf downloads.tgz.5 -C ./data5
tar -xzvf downloads.tgz.6 -C ./data6
tar -xzvf downloads.tgz.7 -C ./data7
tar -xzvf downloads.tgz.8 -C ./data8
tar -xzvf downloads.tgz.9 -C ./data9
tar -xzvf downloads.tgz.10 -C ./data10
tar -xzvf downloads.tgz.11 -C ./data11
tar -xzvf downloads.tgz.12 -C ./data12
tar -xzvf downloads.tgz.13 -C ./data13
tar -xzvf downloads.tgz.14 -C ./data14
tar -xzvf downloads.tgz.15 -C ./data15

