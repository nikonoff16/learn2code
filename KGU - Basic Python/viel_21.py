countries = {'Russia', 'China', 'Korea'}
Autos = {
    'Toyota':{'Russia', 'Korea'}, 
    'Toyamatokanava': set(), 
    'Mazda': {'Russia', 'China', 'Korea'}
    }
for mark in Autos:
    if Autos[mark] == countries:
        print(mark, 'поставляется во все страны')
    elif not Autos[mark]:
        print(mark, 'не импортируется никуда')
    else:
        print(countries.intersection(Autos[mark]))