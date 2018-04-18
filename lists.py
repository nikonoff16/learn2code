#! python3
# -*- coding: utf-8 -*-


number_list = [(foo) for foo in input().split()]
inp_str = []
for egg in number_list:
    if len(number_list) == 1:
        inp_str = [int(number_list[0])]
        #print(number_list[0])
        break
    elif number_list.index(egg) == 0:
        inp_str = inp_str + [str(int(number_list[1]) + int(number_list[-1]))]
        #print(number_list[1] + number_list[-1], end=" ")
    elif number_list.index(egg) == (len(number_list)-1):
        inp_str = inp_str + [str(int(number_list[0]) + int(number_list[-2]))]
       # print(number_list[0] + number_list[-2])
        break
    elif number_list.index(egg) < (len(number_list)-1):
        iter = number_list.index(egg)
        inp_str = inp_str + [str(int(number_list[iter-1]) + int(number_list[iter+1]))]
        #print(number_list[iter-1] + number_list[iter+1], end=" ")
#fuckyoubitch = [print(foo, end=' ') for foo in inp_str]

print(' '.join(inp_str)) 
#print(inp_str)


