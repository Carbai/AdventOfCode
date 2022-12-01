with open('day1.txt') as f1:
    lines = f1.readlines()
    my_dict = {'elves': [],
               'calories': []}

    if lines[0] != "\n":
        my_dict['elves'].append(1)
        my_dict['calories'].append(int(lines[0]))
        blank = False
    else:
        print('Sorry no elves made it! Christmas is ruined.')

    for i in range(1, len(lines)):
        if lines[i] != "\n" and blank == False:
            cal = my_dict.get('calories')
            cal[-1] += int(lines[i])
            my_dict['calories'] = cal

        elif lines[i] != "\n" and blank == True:
            new_elf = len(my_dict['elves']) + 1
            my_dict['elves'].append(new_elf)
            my_dict['calories'].append(int(lines[i]))
            blank = False

        elif lines[i] == "\n":
            blank = True
    snacks = my_dict.get('calories')
    snacks.sort(reverse=True)
    three_top = sum(snacks[0:3])

    print('Highest snacks amount as one elf property:', max(my_dict.get('calories')))
    print('Total snacks owned by the top three snacks holders:', three_top)
