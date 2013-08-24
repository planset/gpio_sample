#!/usr/bin/env python
# -*- coding: us-ascii -*-
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
#
import os
import sys
import math
import time
import datetime
import functools

import wiringpi2
from pylcdsysinfo import LCDSysInfo, TextLines, TextLines, BackgroundColours, TextColours


port = 25

class GPIOReader(object):
    SLEEP_TIME = 0.01
    def __init__(self, owner, port):
        self.owner = owner
        self.port = port

    def onbuttondown(self):
        pass
    def onbuttonpress(self):
        pass
    def onbuttonup(self):
        pass

    def initialize(self):
        wiringpi2.wiringPiSetupGpio()
        wiringpi2.pinMode(port, wiringpi2.GPIO.INPUT)

    def read_wait(self):
        self.initialize()
        status = 0
        while True:
            try:
                val = wiringpi2.digitalRead(port)
                if status == 0 and val == 0:
                    pass
                elif status == 0 and val == 1:
                    status = 1
                    self.onbuttondown()
                elif status == 1 and val == 1:
                    self.onbuttonpress()
                elif status == 1 and val == 0:
                    status = 0
                    self.onbuttonup()
                time.sleep(SLEEP_TIME)
            except KeyboardInterrupt:
                break
            except:
                raise



def main_loop(bg=None, fg=None):
    update_display_period = 1  # number of seconds to wait before updating display
    floor = math.floor  # minor optimization
    
    if bg is None:
        bg = BackgroundColours.BLACK
    if fg is None:
        fg = TextColours.GREEN
    
    line_num = 3

    d = LCDSysInfo()
    d.clear_lines(TextLines.ALL, bg)
    d.dim_when_idle(False)
    d.set_brightness(127)
    d.save_brightness(127, 255)
    d.set_text_background_colour(bg)
    
    class Data(object):
        def __init__(self, d):
            self.d = d
            self.count = 0

    data = Data(owner)

    def onbuttondown(data):
        data.count += 1
        data.d.display_text_on_line(line_num, str(data.count), False, None, fg)

    read_wait(onbuttondown=functools.partial(onbuttondown, owner))


def main(argv=None):
    if argv is None:
        argv = sys.argv
    
    main_loop()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
