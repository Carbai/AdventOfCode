from pathlib import Path
import os
from itertools import permutations

filepath = Path('.')
filename = 'input.txt'

with open(os.path.join(filepath, filename)) as f:
    lines = [line.strip() for line in f.readlines()]
lines = lines[0].split(',')

res = []
for line in lines:
    tmp_res = []
    min_val = line.split('-')[0]
    max_val = line.split('-')[-1]
    if len(min_val) % 2 != 0:
        min_val = str(10**len(min_val))
    if len(max_val) % 2 != 0:
        max_val = str(10**len(max_val))
    range_lst = range(int(min_val[0:len(min_val)//2]),
                      int(max_val[0:len(max_val)//2])+1)
    for val in range_lst:
        val = str(val)
        val = int(2*val)
        if val >= int(min_val) and val <= int(max_val):
            tmp_res.append(val)

    res.extend(list(set(tmp_res)))

res_p2 = []
for line in lines:
    tmp_res = []
    min_val = line.split('-')[0]
    max_val = line.split('-')[-1]
    print('LINE', line)
    for val in range(int(min_val), int(max_val)+1):
        val = str(val)
        combs = sorted([d for d in range(2, len(val)+1)
                       if len(val) % d == 0], reverse=True)
       # print(val, combs)
        for n in combs:
         #   print(n, val, val[0:n], len(val))
            if n == len(val):
                if val.count(val[0]) == len(val):
                    tmp_res.append(int(val))
                  #  print('yes')
            elif val[0:n]*(len(val)//n) == val:
                tmp_res.append(int(val))
    res_p2.extend(list(set(tmp_res)))


print('Sum of invalid ids for p1: ', sum(res))
print('Sum of invalid ids for p2: ', sum(res_p2))
