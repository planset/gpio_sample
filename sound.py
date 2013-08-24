#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import wiringpi2
import time

if wiringpi2.wiringPiSetupGpio() == -1:
    sys.exit(1)

port = 4
wiringpi2.softToneCreate(port)

tones = [262, 293, 329, 349, 391, 440, 494, 523]

def _tone(freq, _time):
    try:
        wiringpi2.softToneWrite(port, freq)
        time.sleep(_time)
    finally:
        wiringpi2.softToneWrite(port, 0)
    time.sleep(0.02)

def tone(no, _time):
    _tone(tones[no], _time)

for no in range(len(tones)):
    tone(no, 1)

