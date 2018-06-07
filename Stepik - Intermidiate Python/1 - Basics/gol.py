#! python3
# -*- coding: utf-8 -*-

import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ': ' + str(msg))

class LoggableList(list, Loggable):
    def append(self, element):
        super().append(element)
        self.log(element)

x = Loggable()

x.log('fuck you')

y = LoggableList()

y.append('fuck off')

print(x, y)