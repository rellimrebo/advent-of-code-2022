# 5.2

with open("5/5.txt") as f:
    first_line = True
    box_stacks = []
    instructions = []
    counter = 0
    boxes_to_move = []
    letters = []

    for line in f.readlines():
        # Check for section of instructions
        
        check = []
        check = line.split()

        if {'move'}.intersection(check): # INTERPRET INSTRUCTIONS
            # Create movement instructions array
            line = line.replace('move','.').replace('from','.').replace(' ','.').replace('to','.').replace('...',',').replace('\n','').replace('..','')
            line = list(line.split(','))

            line = [int(ele) for ele in line] # USE SQUARE BRACKETS DUMMY

            number_to_move = line[0]
            from_stack = line[1] - 1
            to_stack = line[2] - 1

            # Declare blocks to move
            boxes_to_move = box_stacks[from_stack][(-1*number_to_move):]

            # Remove blocks
            box_stacks[from_stack] = box_stacks[from_stack][:len(box_stacks[from_stack]) - number_to_move]

            # Move blocks
            box_stacks[to_stack].append(boxes_to_move)

            # Flatten sublist
            box_stacks[to_stack] = [item for sublist in box_stacks[to_stack] for item in sublist]


        elif {'1'}.intersection(check) or line == '\n':
            pass

        else: # FORM BOX STACKS IN ARRAYS
            line = line.replace(' ','_').replace('____','.').replace('_','').replace('[','').replace(']','').replace('\n','')
            line = list(line)
            length = len(line)
            
            for i in range(length): # 0 1 2
                if first_line == True:

                    if line[i] != '.': 
                        box_stacks.append([line[i]])
                    else:
                        box_stacks.append([])

                    counter += 1
                    if counter == length:
                        first_line = False

                else:
                    if line[i] != '.':
                        box_stacks[i].insert(0,line[i])      
    for i in range(len(box_stacks)):
        letters.append(box_stacks[i][-1:])

    letters = [item for sublist in letters for item in sublist]
    print(''.join(letters))