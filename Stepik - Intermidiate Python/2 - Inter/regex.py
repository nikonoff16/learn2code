import re

# print(re.match)
# print(re.search)
# print(re.findall)
# print(re.sub)

# [] -- можно указать множество подходящих символов
# . ^ $ * + ? { } [ ] ( ) метасимволы
# \d ~ [0-9] -- цифры
# \D ~ [^0-9]
# \s ~ [\t\n\r\f\v] -- пробельные символы
# \S ~ [^ \t\n\r\f\v ]
# \w ~ [a-zA-Z0-9_] -- буквы + цифры + _
# \W ~ [^ a-zA-Z0-9_]
# . ~ заменяет любой символ
## ПОСТСИМВОЛЬНЫЕ МЕТАСИМВОЛЫ
# * ~ ставится после символа и обозначает, что нужно учитывать любое количество этого символа, в том числе нулевое. 
# + ~ тоже, что и звездочка, только нулевое количество не учитывается
# ? ~ учитывает нулевое значение символа или когда он один
# {} - в скобках указывается цифрой, какое количество литералов нужно учитывать. Диапазон значений указывается 
# через запятую без пробела {2,4}



# pattern = r"abc"
# string = "babcd"
# match_object = re.match(pattern, string)
# print(match_object)

# string = "abcd"
# match_object = re.match(pattern, string)
# print(match_object)

# string = "cabcd"
# match_object = re.search(pattern, string)
# print(match_object)

# Первый метасимвол - квадратные скобки с вариантами по типу OR
# pattern = r"a[abc]c"
# string = "accd"
# match_object = re.match(pattern, string)
# print(match_object)

# Пример использования данного метасимвола

# pattern = r"a[abc]c"
# string = "abc, acc, aac"
# all_inclusions = re.findall(pattern, string)
# print(all_inclusions)

# fixed_typos = re.sub(pattern, "abc", string)
# print(fixed_typos)

pattern = r"a[ab]+?a"
string = "abaaba"
match = re.match(pattern, string)
print(match)