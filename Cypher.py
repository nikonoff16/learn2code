#! python3
# -*- coding: utf-8
# создаю строку, которую нужно "зашифровать"
target_str = input()
# цельночисленная переменная, используемая для сравнения предыдущего символа в target_str 
slice_count = -1
cyphered_str = "" 
# строка, в которую записывается вывод /выше/

# создаю цикл для посимвольного прохода строки слева на право
for foo in target_str:
	#добавляю символ в указанную строку для последующего 
	#сохранния или изменения
	cyphered_str.add(foo)
	if slice_count >= 0:
		if cyphered_str[-1] == '0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':
			continue
	
	
	# исключаю ошибку алгоритма при проходе первого символа - прогрвмма выполняется, если slice_count не в начальнлй позиции
	if slice_count != -1:
		# создаю клон slice_count для просчета повторяющихся сисволов в следующем цикле
	
		egg = slice_count
		# создаю счетчик, запоминающий количество одинаковых сисволов подряд с ненулевым значением
		count = 0
		# создаю цикл вычисляющий количество подряд идущих сиволов, направленный справа на лево. 
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
		cyphered_str.add(count)
	
	
			
				
				
			
				

		
	else:
		cyphered_str = target_str[0]
		slice_count += 1
		
	
	
