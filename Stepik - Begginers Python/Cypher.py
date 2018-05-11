#! python3
# -*- coding: utf-8 -*-

# создаю строку, которую нужно "зашифровать"
target_str = input()

# принудительно изменяем регистр на малый
#target_str = target_str.lower()
# цельночисленная переменная, используемая для итерирования цикла
slice_count = 0
# строка, в которую записывается вывод
cyphered_str = "" 
# счетчик
shiphr = 1

"""
Первый цикл обрабатывает одиночные символы и недопускает ошибки вида:
- единственный символ в строке
- выход индекса строки за рамки
"""
while slice_count < len(target_str):
	current_symbol = target_str[slice_count]
	shiphr = 1
	if slice_count == (len(target_str) - 1):
		if len(target_str) == 1:
			cyphered_str = cyphered_str + current_symbol + str(shiphr)
			break
		elif target_str[-2] == target_str[-1]:
			break
		else:
			cyphered_str = cyphered_str + current_symbol + str(shiphr)
			break
# обработка одиночных символов
	elif current_symbol != target_str[slice_count +1]:
		cyphered_str = cyphered_str + current_symbol + str(shiphr)
		slice_count += 1
		continue
	elif current_symbol == target_str[slice_count +1]:
		cyphered_str = cyphered_str + current_symbol
		shiphr = 1
#Второй цикл обрабатывает последовательности одинаковых символов
#Он также имеет условие, не допускающее выход за границы строки.
		while True:
			if slice_count == (len(target_str) - 1):
				cyphered_str = cyphered_str + str(shiphr)
				break
			elif current_symbol == target_str[slice_count +1]:
				shiphr += 1
				slice_count += 1
			else:
				cyphered_str = cyphered_str + str(shiphr)
				slice_count += 1
				break

# По завершении цикла напечатать получившийся шифр
print(cyphered_str)
	
