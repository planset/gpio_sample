#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wiringpi2
import time

# GPIOの指定をGPIO番号に設定する。
wiringpi2.wiringPiSetupGpio()

# 使用するGPIOポート
port = 4

# 指定のGPIOの出力方向を決める。
# GPIO.INPUT, GPIO.OUTPUT, GPIO.PWM_OUTPUT, GPIO_CLOCK
wiringpi2.pinMode(port, wiringpi2.GPIO.OUTPUT)

val = 0
while True:
    try:
        wiringpi2.digitalWrite(port, val)
        val = 1 - val
        time.sleep(0.1)
    except KeyboardInterrupt:
        break
    except:
        raise

wiringpi2.digitalWrite(port, 0)
wiringpi2.pinMode(port, wiringpi2.GPIO.INPUT)

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
