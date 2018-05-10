#! python3
# -*- coding: utf-8 -*-

import requests


with open('dataset_3378_2.txt', 'r') as inf:
    url = inf.read()
print(url)
r = requests.get(url)
open('854.txt', 'wb').write(r.content)
print(r.text)