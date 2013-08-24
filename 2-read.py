#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wiringpi2
import time

# GPIOの指定をGPIO番号に設定する。
wiringpi2.wiringPiSetupGpio()

# 使用するGPIOポート
port = 25

# 指定のGPIOの出力方向を決める。
# GPIO.INPUT, GPIO.OUTPUT, GPIO.PWM_OUTPUT, GPIO_CLOCK
wiringpi2.pinMode(port, wiringpi2.GPIO.INPUT)

val = 0
while True:
    try:
        val = wiringpi2.digitalRead(port)
        print val
        time.sleep(0.1)
    except KeyboardInterrupt:
        break
    except:
        raise

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
