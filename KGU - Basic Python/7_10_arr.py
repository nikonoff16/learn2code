"""
7.10
Вам дан словарь, состоящий из пар слов. 
Каждое слово является синонимом к парному ему слову. 
Все слова в словаре различны. 
Для последнего слова из словаря определите его синоним.
"""

k_v_count = int(input("Введите количество запросов на обработку: "))
wortbuch = {}
value_set = set()
for pair in range(k_v_count):  # Итерируемся по количеству позиций в словаре
    key = input("\nВведите ключ словаря: ")
    value = set([foo for foo in input("Введите синонимы через пробел: ").split()])
    # wortbuch[key] = value
    check = value_set.intersection(value)
    value_set = value_set.union(value)
    new = value.difference(check)
    if key not in wortbuch.keys():
        if not check:
            print("Значения уникальны для слова", key, "и внесены в словарь под этим ключом.")
            wortbuch[key] = new
        elif check == value:
            print("Все введеные значения уже пристутсуют в словаре, нет нужды создавать дублирующую статью.")
        else:
            print("Лишь значения", new, "не имеют упоминания в прочих статьях словаря. Они закреплены за ключом", key)
            wortbuch[key] = new
    else:
        if not check:
            print("Значения уникальны и добавлены к существующему ключу", key)
        elif check == value:
            print("Все введеные значения уже пристутсуют в словаре и добавлены не будут")
        else:
            print("Лишь значения", new, "не имеют упоминания в прочих статьях словаря. Они добавлены ко ключу", key)
        wortbuch[key] = wortbuch[key].union(new)

print("\nСоздание словаря закончено. Вот его полная упорядоченная версия: ")
for k in sorted(wortbuch.keys()):
    print("Ключ:", k, "Значение:", wortbuch[k])
      




