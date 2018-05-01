#!python3
# -*- coding: utf-8 -*-

import commands8
from commands8 import *


time_1= Time.stamp()
print('*' * 100000)
time_2= Time.stamp()
print(time_1, time_2)
print(Time.delta(time_1, time_2))