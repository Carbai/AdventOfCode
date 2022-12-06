import time
start=time.time()

with open ('input.txt') as ifile:
    LINES = ifile.read()

def is_marker(word: str) -> bool:
    #return len(set(word)) == len(word)   ## optimized option -- suggested solution
    count=0
    for lett in word:
        count += (word.count(lett))
    return count == len(word)

def find_marker(lines: str, range_val: int) -> int:
    for i in range(len(lines)-range_val):
        if is_marker(lines[i:i+range_val]):         
            return (i+range_val)

def part_one(lines: str, str_len: int) -> int:
    return find_marker(lines, str_len)

def part_two(lines: str, str_len: int) -> int:
    return find_marker(lines, str_len)
    
print(part_one(LINES, 4))
print(part_two(LINES, 14))
print(f'execuded in {time.time()-start}')
