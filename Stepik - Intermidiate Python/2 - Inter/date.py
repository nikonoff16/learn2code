#! python3
# -*- coding: utf-8 -*-

class MoreOrlessThanThreeError(Exception):
    pass
import datetime
while True:
    try:
        fuck = tuple(int(foo) for foo in input().split())
        if len(fuck) != 3:
            raise MoreOrlessThanThreeError("Date format is not correct for counting. Please, try again")

    except (ValueError, TypeError):
        print("You've entered incorrect symbols. Please, try again")
        continue
    else:
        break


year, month, day = fuck[0], fuck[1], fuck[2]
date = datetime.date(year, month, day)

newdate = date + datetime.timedelta(days=int(input()))

prin_date = newdate.__str__()
prin_date = [int(foo) for foo in prin_date.split("-")]
for foo in prin_date:
    print(foo, end=' ')
