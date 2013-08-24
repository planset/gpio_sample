#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wiringpi2
import time

wiringpi2.wiringPiSetupGpio()

port = 18

wiringpi2.softServoSetup(port, -1, -1, -1, -1, -1, -1, -1)

wiringpi2.softServoWrite(port, -250)
time.sleep(1)

for i in range(-250, 1250, 100):
    wiringpi2.softServoWrite(port, i)
    time.sleep(0.2)

time.sleep(1)

