# 3.2

with open("3/3.txt") as f:
    group_search = []
    badges = []
    line_count = 0

    for line in f.readlines():
        line = line.strip()
        group_search.append(line)

        line_count += 1

        if line_count == 3:
            badges.append(set(group_search[0]).intersection(group_search[1],group_search[2]))

            group_search.clear()
            line_count = 0

    badges = [item for sublist in badges for item in sublist]

    translated_badges = []

    for item in badges:
        if ord(item) > 90:
            translated_badges.append(ord(item) - 96)
        else: 
            translated_badges.append(ord(item) - 38)
    
    print(sum(translated_badges))