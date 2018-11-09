# countries = {'Russia', 'China', 'Korea'}
# Autos = {
#     'Toyota':{'Russia', 'Korea'}, 
#     'Toyamatokanava': set(), 
#     'Mazda': {'Russia', 'China', 'Korea'}
    # }
count = int(input('Какое количество автомобильных марок вы собираетесь внести: '))
countries = set()
autos = {}
while count != 0:
    auto_seria = input('Введите имя марки: ')
    auto_import = input('Введите страны экспорта через пробел: ')
    if auto_import == '':
        autos[auto_seria] = set()
    else:
        autos[auto_seria] = set(auto_import.split(' '))
    countries = countries.union(autos[auto_seria])
    count -= 1

# print(countries, autos)
for mark in autos:
    if not autos[mark]:
        print(mark, 'не поставляется никуда')
    elif autos[mark] == countries:
        print(mark, 'поставляется во все страны')
    else:
        where_imp = countries.intersection(autos[mark])
        print(mark, 'поставляется в', ', '.join(list(where_imp)))
    
