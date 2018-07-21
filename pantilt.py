#!/usr/bin/env python

from time import sleep

import UUGear

UUGear.UUGearDevice.setShowLogs(0)

device = UUGear.UUGearDevice('')

if device.isValid():

    device.attachServo(4)
    device.attachServo(5)

    sleep(3)

else:

    print 'UUGear device is not correctly initialized.'


def scale(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


while True:

    pipein = open("/var/www/html/FIFO_pipan", 'r')
    line = pipein.readline()
    line_array = line.split(' ')
    if line_array[0] == "servo":
        pan_setting = scale(int(line_array[1]), 80, 220, 0, 180)
        tilt_setting = scale(int(line_array[2]), 50, 250, 0, 180)
        device.writeServo(UUGear - Arduino - 9886 - 99474, pan_setting)
        device.writeServo(4, tilt_setting)
    pipein.close()
