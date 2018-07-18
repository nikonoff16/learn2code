#! python3
# -*- coding: utf-8 -*-

import json
import requests
from requests import Response


def numbers_api(number):
    api = 'http://numbersapi.com/' + number + '/math?json'
    fact = requests.get(api)
    data = fact.json()
    return data


with open("dataset_24476_2.txt", "r") as numbers:
    for cypher in numbers:
        cypher = cypher.rstrip()
        json_data = numbers_api(cypher)
        if json_data['found']:
            print("Interesting")
        else:
            print("Boring")