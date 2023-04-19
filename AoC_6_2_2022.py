# 6.2

with open("6/6.txt") as f:
    code = ''
    for line in f.readlines():
        code = line
    for i in range(len(code)-14):
        check = set(code[i:(i+14)])
        if len(check) == 14:
            print(i+14)
            break