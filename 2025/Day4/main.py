from pathlib import Path
import os
from itertools import product

with Path("input.txt").open() as f:
    lines = [line.strip() for line in f.readlines()]


def calc_neighbors(pos):
    r, c = pos
    return [
        (nr, nc)
        for nr, nc in product([r - 1, r, r + 1], [c - 1, c, c + 1])
        if (nr, nc) != pos
    ]


def should_remove(neigs, paper_set):
    return sum(1 for neig in neigs if neig in paper_set) < 4


papers = [(i, j) for i, row in enumerate(lines)
          for j, char in enumerate(row) if char == '@']

res_p1 = []
res_p2 = len(papers)
old_len = -1
papers_set = set(papers)
while len(papers) != old_len:
    old_len = len(papers)
    to_drop = set()
    res = 0
    for paper in papers:
        neigs = calc_neighbors(paper)
        if should_remove(neigs, papers_set):
            res += 1
            to_drop.add(paper)
    res_p1.append(res)
    papers = [pos for pos in papers if pos not in to_drop]
    papers_set = set(papers)

print('Solution to p1: ', res_p1[0])
print('Solution to p1:', res_p2-len(papers))
