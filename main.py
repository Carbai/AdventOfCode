with open('day1.txt') as f1:
    lines = f1.readlines()
my_dict = dict()

if lines[0] != "\n":
    my_dict[0] = int(lines[0])
    blank_line = False
else:
    print('Sorry no elves made it! Christmas is ruined.')
    exit()

for i in range(1, len(lines)):
    if lines[i] != "\n" and blank_line == False:
        my_dict[len(my_dict)-1] = my_dict[len(my_dict)-1] + int(lines[i])

    elif lines[i] != "\n" and blank_line == True:

        my_dict[len(my_dict)] = len(my_dict)

        my_dict[len(my_dict)-1] = int(lines[i])
        blank_line = False

    elif lines[i] == "\n":
        blank_line = True

print(my_dict)
sorted_snacks = dict(sorted(my_dict.items(), key=lambda item: item[1]))
three_richest_elves = list(sorted_snacks.items())[-3:]
tot = [sum(i) for i in zip(*three_richest_elves)]
print("Highest amount of snacks as single elf property:", three_richest_elves[-1][-1])
print("Highest amount of snacks as three richest elves property:", tot[-1])


