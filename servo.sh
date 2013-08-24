#!/bin/bash
sudo killall servod
sudo servod

servo=2
pw=0

for i in `seq 1 24` ; do
	echo $servo=$pw > /dev/servoblaster
	sleep 0.1
	pw=`expr $pw + 10`
done

sudo killall servod
