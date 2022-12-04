with open ("example.txt") as ifile:
    lines = ifile.readlines()
    for i in range(len(lines)):
        lines[i]= lines[i].split(",")
  
def parse_turns(turns: list) -> tuple:
    range_1 = []
    range_2 = []
    for turn in turns:   
        range_1.append(range(int(turn[0].split("-")[0]),int(turn[0].split("-")[1])+1))
        range_2.append(range(int(turn[1].strip("\n").split("-")[0]),int(turn[1].strip("\n").split("-")[1])+1))
    return (range_1, range_2)

def part_one(turns: list) -> int:
    overlap = 0
    elf_1, elf_2 = parse_turns(turns)
    for item1, item2 in zip(elf_1,elf_2):
        if set(item1).issubset(item2) or set(item2).issubset(item1):
            overlap +=1
    return overlap

def part_two(turns: list) -> int:
    overlap = 0
    elf_1, elf_2 = parse_turns(turns)
    for item1, item2 in zip(elf_1,elf_2):    
        if len(set(item1).intersection(item2)) != 0:
            overlap += 1        
    return overlap

print(part_one(lines))
print(part_two(lines))
