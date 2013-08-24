#!/bin/sh
servo=2  #GPIO18
pw=40    #start
for i in `seq 1 20` ; do
  echo $servo=$pw >/dev/servoblaster
  sleep 0.1
  pw=`expr $pw + 10`
done
