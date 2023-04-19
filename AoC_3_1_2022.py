# 3.1

with open("3/3.txt") as f:
    half_line_length = 0
    common_items = []

    for line in f.readlines():
        line = line.strip()
        half_line_length = int(len(line)/2)
        first_half = set(line[:half_line_length])
        second_half = set(line[half_line_length:])

        common_items.append(first_half.intersection(second_half))

    common_items = [item for sublist in common_items for item in sublist]
    
    translated_items = []

    for item in common_items:
        if ord(item) > 90:
            translated_items.append(ord(item) - 96)
        else: 
            translated_items.append(ord(item) - 38)
    
    print(sum(translated_items))