# 4.2

with open("4/4.txt") as f:
    duplicate_assignments = 0

    for line in f.readlines():
        line = line.replace('-',',').replace('-',',').replace('\n','')
        line = line.split(',')
        
        line = [int(string) for string in line]

        if line[0] <= line[2] and line[2] <= line[1] or line[0] <= line[3] and line[3] <= line[1]:
            duplicate_assignments += 1

        elif line[2] <= line[0] and line[0] <= line[3] or line[2] <= line[1] and line[1] <= line[3]:
            duplicate_assignments += 1

    print(duplicate_assignments)