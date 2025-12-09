from pathlib import Path
from itertools import islice
import math
import re

with Path("input.txt").open() as f:
    lines = [line.replace('\n','') for line in f.readlines()]
size=len(lines)
inp={(i,j):l for i,line in enumerate(lines) for j,l in enumerate(line)}
queue=[key for key in inp.keys() if inp[key]=='S']
n_split=0
nodes=[]
timelines=0
while queue: 
     
    pos=queue.pop()
    nodes.append(pos)
    new_pos=(pos[0]+1,pos[1])
    
    if new_pos not in inp.keys() or new_pos in nodes:       
        continue
    if inp[new_pos]=='.':
        queue.append(new_pos)
    else:
        n_split+=1
        new_pos=[(pos[0]+1,pos[1]-1),(pos[0]+1,pos[1]+1)]
        new_pos=[p for p in new_pos if p in inp.keys()]
        queue.extend(new_pos)

print('Solution to part one: ', n_split)
    