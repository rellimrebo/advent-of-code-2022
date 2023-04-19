# 1
import os

os.system('cls')

with open("1/1.txt") as f:
    #print(f.readlines()) 

    # print(num_lines)


    sums = [0]
    current_elf = 0
    # numbers = f.readlines

    for line in f.readlines():
        if line == '\n':
            sums.append(0)
            current_elf += 1
        else:
            sums[current_elf] += int(line[:-1])

    sums.sort()
    top_sums = sums[-3:]
    print(sum(top_sums))



