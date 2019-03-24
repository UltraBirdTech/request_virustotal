#!bin/sh
echo '####### CREATE FOLDER ###################'
echo 'create downloads folder is start.'
mkdir /home/honey/downloads
mkdir /home/honey/dionaea_malwares
echo 'create downloads foler is finished.'

echo '####### COPY FILES ###################'
echo 'copy folder is start.'
cp /data/cowrie/downloads.*.gz /home/honey/downloads/
cp /data/dionaea/binaries.*.gz /home/honey/dionaea_malwares/
echo 'copy folder is finish.'

echo '####### TAR FILES ###################'
echo 'create tar file start.'
tar -zcvf /home/honey/downloads.tar.gz /home/honey/downloads/
tar -zcvf /home/honey/dionaea_malwares.tar.gz /home/honey/dionaea_malwares/
echo 'create tar file finsih.'
