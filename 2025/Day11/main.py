from pathlib import Path
from functools import cache
with Path('test1.txt').open() as f:
    lines=[line.split(':') for
           line in f.read().splitlines()]

my_dict={line[0]:line[1].strip().split() for line in lines}

queue=['you'] 
n=0
while queue:
    p=queue.pop()
    if p == 'out':
        n+=1
    else:
        queue.extend(my_dict[p])       
print('Solution to part one: ', n) ##753

@cache
def find_paths(start, end):
    n=0
    if start==end:
        return 1
    try:
        for node in my_dict[start]:
            n+=find_paths(node,end)
    except KeyError:
        return 0
    return n

print('Solution to part two: ', find_paths('svr','fft')*find_paths('fft','dac')*find_paths('dac','out'))