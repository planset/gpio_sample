#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import wiringpi2
import time

# GPIOの指定をGPIO番号に設定する。
if wiringpi2.wiringPiSetupGpio() == -1:
    sys.exit(1)

# 使用するGPIOポート
port = 18

# 指定のGPIOの出力方向を決める。
# GPIO.INPUT, GPIO.OUTPUT, GPIO.PWM_OUTPUT, GPIO_CLOCK
wiringpi2.pinMode(port, wiringpi2.GPIO.PWM_OUTPUT)

SLEEP_TIME = 0.01

val = 0
while True:
    try:
        for pw in range(1024):
            wiringpi2.pwmWrite(port, pw)
            time.sleep(SLEEP_TIME)
        for pw in range(1024-1, 0-1, -1):
            wiringpi2.pwmWrite(port, pw)
            time.sleep(SLEEP_TIME)
    except KeyboardInterrupt:
        break
    except:
        raise

sys.exit(0)

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
