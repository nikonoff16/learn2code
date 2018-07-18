#! python3
# -*- coding: utf-8 -*-

import csv

crime_type = {}

with open("Crimes.csv") as csv_sheet:
    crime = csv.reader(csv_sheet)
    for cr in crime:
        if '2015' in cr[2]:
            # We need [5] position to find Primary Type
            if cr[5] not in crime_type.keys():
                crime_type[cr[5]] = 1
            else:
                crime_type[cr[5]] += 1

the_most_popular = ''
count = 0
for kind_of in crime_type.keys():
    if crime_type[kind_of] > count:
        count = crime_type[kind_of]
        the_most_popular = kind_of
print(crime_type)
print(the_most_popular, count)