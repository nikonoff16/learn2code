


# for line in sys.stdin:
#     line = line.rstrip()
#     pattern = r"\bcat\b"
#     if re.search(pattern, line):
#         print(line)

# str_list = []
# while True:
#     stroke = input()
#     if len(stroke) != 0:
#         str_list.append(stroke)
#     else:
#         break


# for line in str_list:
#     line = line.rstrip()
#     pattern = r"\bcat\b"
#     if re.search(pattern, line):
#         print(line)


# for line in sys.stdin:
#     line = line.rstrip()
#     pattern = r"с"
#     if re.search(pattern, line):
#         print(line)

# lst_str = []
# for line in sys.stdin:
#     line = line.strip()
#     if len(line) != 0:
#         lst_str.append(line)
#     else:
#         break
#     if len(lst_str) == random.choice(1,2):
#         break
# for foo in lst_str:
#     newline = re.sub(r"human", "computer", foo)
#     print(newline)

# lst_str = []
# for foo in range(2):
#     line = input().strip()
#     if len(line) != 0:
#         lst_str.append(line)

# for line in sys.stdin:
#     firstline = line.strip()
#     secondline = line.strip()
#     oldpattern = r"human"
#     pattern = r"computer"
#     print(re.sub(oldpattern, pattern, firstline))
#     print(re.sub(oldpattern, pattern, secondline))

# for line in sys.stdin:
#     line = 
#     line.replace("human", "computer")
#     print(line)
    
pattern = r'(\w)\1+'

for line in sys.stdin:
    print(re.sub(pattern, r'\1', line.rstrip()))