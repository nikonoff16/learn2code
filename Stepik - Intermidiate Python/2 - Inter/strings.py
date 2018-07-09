# print('abc' in 'abcde')
# print('abc' in 'abdef')

# print('eabcd'.find('abc'))
# # print(str.find.__doc__)

# s = 'Я жру яблоко и думаю о том, как стать кодером'

# print(s.startswith(('Я жру', 'Я сру', 'я пью')))
# # print(s.startswith.__doc__)

# print(s.endswith(('кодером', 'я пью')))
# # print(s.endswith.__doc__)

# s = 'Человек в черном подошел к корчащемуся от боли Тедди и выстрелил в сломанную руку.'

# print(s.lower())
# print(s.upper())
# print(s.count("в"))
# print(s.lower().count("в"))

# s = "1,2,3,4"

# print(s)
# print(s.replace(',', ', '))
# print(s.split(',', 2))
# print(s.split.__doc__)

# numbers = map(str, [1, 2, 3, 4, 5])
# print(numbers)
# print(repr(" ".join(numbers)))

# capital = "London is the capital of Great Britain"
# template = "{1} is the capital of {0}"
# print(template.format("London", "Great Britain"))
# print(template.format("Moscow", "Russia"))

# # print(template.format.__doc__)

# template = "{capital} is the capital of {country}"
# # print(template.format(capital="London", country="Great Britain"))
# fuck = template.format(country="Russia", capital="Moscow")
# print(fuck)

import requests

template = "Response from {0.url} with code {0.status_code}"

res = requests.get("https://docs.python.org/3.5/")
print(template.format(res))

res = requests.get("https://docs.python.org/3.5/random")
print(template.format(res))