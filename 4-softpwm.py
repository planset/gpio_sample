#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import wiringpi2
import time

# GPIOの指定をGPIO番号に設定する。
if wiringpi2.wiringPiSetupGpio() == -1:
    sys.exit(1)

# 使用するGPIOポート
port = 4

RANGE = 100 # PWMに指定する値の最大値

# softPwmの設定 
wiringpi2.softPwmCreate(port, 0, RANGE)  # ポート、初期値、最大値

SLEEP_TIME = 0.01

val = 0
while True:
    try:
        for pw in range(100):
            wiringpi2.softPwmWrite(port, pw)
            time.sleep(SLEEP_TIME)
        for pw in range(100-1, 0-1, -1):
            wiringpi2.softPwmWrite(port, pw)
            time.sleep(SLEEP_TIME)
    except KeyboardInterrupt:
        break
    except:
        raise

sys.exit(0)

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
