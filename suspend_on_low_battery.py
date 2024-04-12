#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
################################################################################
#                                                                              #
# suspend_on_low_battery                                                       #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program suspends a computer when low battery is detected.               #
#                                                                              #
# copyright (C) 2024 William Breaden Madden                                    #
#                                                                              #
# This software is released under the terms of the GNU General Public License  #
# version 3 (GPLv3).                                                           #
#                                                                              #
# This program is free software: you can redistribute it and/or modify it      #
# under the terms of the GNU General Public License as published by the Free   #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# This program is distributed in the hope that it will be useful, but WITHOUT  #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or        #
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for     #
# more details.                                                                #
#                                                                              #
# For a copy of the GNU General Public License, see                            #
# <http://www.gnu.org/licenses>.                                               #
#                                                                              #
################################################################################
'''

import subprocess
import time

__version__ = '2024-04-09T2219Z'

def get_battery_percentage():
    try:
        result = subprocess.check_output(['upower', '-i', '/org/freedesktop/UPower/devices/battery_BAT0'])
        result = result.decode('utf-8')
        for line in result.split('\n'):
            if 'percentage' in line:
                percentage_str = line.split(':')[1].strip()
                return int(percentage_str.rstrip('%'))
    except subprocess.CalledProcessError:
        return 'unable to get battery information'

while True:
    battery_percentage = get_battery_percentage()
    if isinstance(battery_percentage, int):
        print(f'battery percentage: {battery_percentage}%')
        if battery_percentage <= 5:
            subprocess.run(['systemctl', 'suspend'])
    else:
        print(battery_percentage)
    time.sleep(30)
