# 6.1

with open("6/6.txt") as f:
    code = ''
    for line in f.readlines():
        code = line

    for i in range(len(code)-4):
        check = set(code[i:(i+4)])
        
        if len(check) == 4:
            print(i+4)
            break