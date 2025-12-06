from pathlib import Path
from itertools import islice
import math
import re

with Path("test.txt").open() as f:
    lines = [line.replace('\n','') for line in f.readlines()]

lines_=list(map(list, zip(*lines[:-1])))

def process_p1(lst):
    lst = [re.sub(r'\s+', ' ', line.strip()) for line in lst]
    new_line=[]
    for l in lst[:-1]:
        new_line.append([int(j) for j in l.split()])
    return list(map(list, zip(*new_line)))

def process_p2(lst):
    new_list=[]
    for l in lst:
        new_list.append(''.join([i for i in l]))
    new_list.append('   ')
    split_ndx=[n for n,l in enumerate(new_list) if l.strip()=='']
    curr_ndx=0
    l=[]
    for ndx in split_ndx:
        l.append([int(i) for i in new_list[curr_ndx:ndx]])
        curr_ndx=ndx+1
    return l

def solve(lst):
    res=[]
    operations=[op.split() for op in lst[-1]][0]
    for n,op in enumerate(operations): 
        if op=='+':
            res.append(sum(lst[n]))
        else:
            res.append(math.prod(lst[n]))
    return sum(res)


list_p2=process_p2(lines_)
list_p2.append([lines[-1]])
list_p1=process_p1(lines)
list_p1.append([lines[-1]])
print('Solution to part one:', solve(list_p1))
print('Solution to part two:', solve(list_p2))

