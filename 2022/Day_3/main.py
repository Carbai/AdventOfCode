with open('input.txt') as f1:
    LINES = f1.readlines()

#part one
def lett_to_num( char: str) -> int:
    if char.islower():
        return ord(char) - 96
    return ord(char.lower()) - 96 + 26

def part_one( lines: list) -> int:
    score = 0
    for line in lines:
        first_half = line[slice(0,len(line)//2)]
        second_half = line[slice(len(line)//2,len(line))]
        common_value = "".join(set(first_half).intersection(second_half))
        score += lett_to_num(common_value)
    return score

#part two:
def part_two( lines: list) -> int:
    score = 0
    for i in range(len(lines)+1):
     
        if i % 3 == 0 and i != 0:
            first = set(lines[i-1].strip())
            second = set(lines[i-2].strip())
            third = set(lines[i-3].strip())
            common_item = list(first & second & third)[0]
            if common_item is not None:
                score += lett_to_num(common_item)
            
    return score

#print(part_one(LINES), len(LINES))
print(part_two(LINES))


   
