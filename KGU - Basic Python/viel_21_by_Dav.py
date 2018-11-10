"""Известны марки машин, изготовляемых в данной стране и импортируемых за
рубеж. Даны некоторые N стран. Определить для каждой из марок, какие из них
были:
• доставлены во все страны;
• доставлены в некоторые из стран;
• не доставлены ни в одну страну."""
print(""" Марки:  Toyota        Ford      Chevrolet        Nissan    Jeep
         Hyundai       KIA       Mercedes-Benz    Citroen  
         Volkswagen    Tesla     Land Rover       Volvo  
         Suzuki        Peugeot   УАЗ              Audi


 Страны: Россия   Австралия   Люксембург
""")

Marka={'Toyota', 'Ford', 'Chevrolet', 'Nissan', 'Hyundai', 'KIA', 'Mercedes-Benz', 'Citroen',
       'Volkswagen', 'Tesla', 'Land Rover', 'Volvo',  'Suzuki', 'Peugeot', 'УАЗ', 'Jeep', 'Audi'}
Russia={'Toyota', 'Ford', 'Chevrolet', 'Nissan', 'Hyundai', 'KIA', 'Mercedes-Benz'}
Australia={'Toyota', 'Ford', 'Land Rover', 'Volvo',  'Suzuki', 'УАЗ', 'Jeep', 'Audi'}
Luxembourg={'Ford', 'Chevrolet', 'Nissan', 'Hyundai', 'KIA', 'Tesla', 'Land Rover'}
werty=Russia&Australia&Luxembourg
print()
print("Произведено в России:",Russia)
print()
print("Произведено в Австралии:",Australia)
print()
print("Произведено в Люксембург:",Luxembourg)

print()
input(" <Enter> Для просмотра отчета") 
print("Доставлены во все страны:", werty)
print()
print("Доставлены в некоторые из стран:", (Russia-werty)|(Australia-werty)|(Luxembourg-werty))
print()
print("Не доставлены ни в одну страну:",Marka-(Russia|Australia|Luxembourg))
input()
