#! python3
# -*- coding: utf-8 -*-

# создаю строку, которую нужно "зашифровать"
target_str = input()
# цельночисленная переменная, используемая для сравнения предыдущего символа в target_str 
slice_count = -1
cyphered_str = "" 
# строка, в которую записывается вывод /выше/

# создаю цикл для посимвольного прохода строки слева на право
for foo in target_str:
# Создаю условие, которое отсеивает несколько символов в ряд, уже сжатых
	if slice_count >= 0:
		if cyphered_str[-1].isnumeric() == True :
			print(cyphered_str[-1].isnumeric())
			if foo == target_str[slice_count]:
				continue
#добавляю символ в указанную строку для последующего сохранния или изменения
	cyphered_str = cyphered_str + foo
	print(cyphered_str)

	
	
	# исключаю ошибку алгоритма при проходе первого символа - программа выполняется, если slice_count не в начальнлй позиции
	if slice_count >=0:
		# создаю клон slice_count для просчета повторяющихся символов в следующем цикл
		egg = slice_count
		# создаю счетчик, запоминающий количество одинаковых си волов подряд с ненулевым значением
		count = 0
		# создаю цкл вычисляющий количество подряд идущих сиволов, направленный справа налево. 
		while True:
			if foo == target_str[egg]:
				count += 1
				if egg < (len(target_str)-1):
					egg += 1
				else:
					break
			else:
				break
		if count > 1:
			cyphered_str = cyphered_str + str(count)

	
		
	slice_count += 1
	print(slice_count)
# По завершении цикла напечатать получившийся шифр
print(cyphered_str)
	
