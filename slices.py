#! python3
# -*- coding: utf-8 -*-

genome = input()

length = len(genome)

g_count = genome.lower().count('g')
c_count = genome.lower().count('c')

print(((g_count+c_count)/length)*100)
