from pathlib import Path
from itertools import islice

with Path("input.txt").open() as f:
    lines = [line.strip() for line in f.readlines()]

blank = lines.index('')
ranges = [(int(i), int(j)) for val in lines[:blank]
          for i, j in (val.split('-'),)]
ingredients = [int(x) for x in lines[blank+1:]]


def is_fresh(x, ranges):
    return any(lo <= x <= hi for lo, hi in ranges)


def count_fresh(lo, hi):
    return hi-lo+1


res_p1 = sum(1 for ing in ingredients if is_fresh(ing, ranges))
sorted_ranges = sorted(ranges)
curr_lo, curr_hi = sorted_ranges[0]
res_p2 = curr_hi-curr_lo+1
for lo, hi in sorted_ranges[1:]:
    if lo > curr_hi:
        res_p2 += count_fresh(curr_lo, curr_hi)
        curr_lo, curr_hi = lo, hi
    else:
        curr_hi = max(curr_hi, hi)
res_p2 += count_fresh(curr_lo, curr_hi)
print('Solution to p1: ', res_p1)  # 679
print('Solution to p2: ', res_p2)  # 358155203664116
