#! python3
# -*- coding: utf-8 -*-

import requests

r = requests.get('https://stepic.org/media/attachments/course67/3.6.2/899.txt')
print(r.text)
string_quantity = r.text.splitlines()
print(len(string_quantity))