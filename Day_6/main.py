with open ('input.txt') as ifile:
    LINES = ifile.readlines()

def find_marker(lines: str, range_val: int) -> int:
    found_marker = False
    for i in range(2, len(lines)-range_val-2):
        count=0
        for lett in lines[i: i+range_val]:
            if found_marker == False:
                count += (lines[i: i+range_val].count(lett))
        if count == range_val:
            found_marker = True
            break
    return (i+range_val-2)

def part_one(lines: str, str_len: int) -> int:
    return find_marker(lines, str_len)

def part_two(lines: str, str_len: int) -> int:
    return find_marker(lines, str_len)
    
print(part_one(str(LINES), 4))
print(part_two(str(LINES), 14))