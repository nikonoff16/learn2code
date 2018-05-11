#! python3
# -*- coding: utf-8 -*-

def modify_list(l):
    l[:] = [i//2 for i in l if not i % 2]

# def modify_list(l):
    # check = 0
    # len(l)
    # while check < len(l):
        # if l[check] % 2 != 0:
            # l.remove(l[check])
        # else:
            # check += 1
    # for egg in range(len(l)):
        # l[egg] = int(l[egg] / 2)
        
			
	
lst = [10, 5, 8, 3]
print(modify_list(lst))
print(lst)
modify_list(lst)
print(lst)

# def modify_list(l):
	# l = list
	# for foo in range(len(list)):
		# if l[foo] % 2 == 0:
			# number = (l[foo])/2
			
			# list.append(number)
			# check += 1
	# list = l		
# lst = [1, 2, 3, 4, 5, 6]
# print(modify_list(lst))
# print(lst)