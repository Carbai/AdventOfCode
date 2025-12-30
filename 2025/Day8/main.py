from pathlib import Path
import numpy as np
import math 
with Path('test.txt').open() as f:
    inp=[tuple(map(int,line.split(','))) 
        for line in f.read().splitlines()]
print('prova',inp)

sim_matrix=np.empty(shape=(len(inp),len(inp)))
closest_dict={}
val=float('inf')
neig=tuple()
for n,p1 in enumerate(inp[:-1]):
    for m,p2 in enumerate(inp[n+1:]):
        dist=np.linalg.norm(np.array(p2)-np.array(p1))
        print('step', p1, p2, dist)
        if dist<val:
            val=dist
            neig=p2
            print('updated', val, neig)
    val=float('inf')
    closest_dict[p1]=p2


        
print(closest_dict)