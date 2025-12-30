from pathlib import Path
from functools import cache

with Path('input.txt').open() as f:
    lines=f.read().split('\n\n')

packages=[pack for pack in lines if '#' in pack]
box=[l for l in lines if '#' not in l][0].split('\n')
n_packages=[pack.count('#') for pack in packages]
map_p1=[(int(l.split(':')[0].split('x')[0])*int(l.split(':')[0].split('x')[-1]),list(map(int,l.split(':')[1].split()))) for l in box]
def is_contained(box,pack):
    pack=sum(i*j for i,j in zip(pack,n_packages))
    return box>pack
part1=0
for s in map_p1:
    if is_contained(s[0],s[1]):
        part1+=1

print('Solution to part one:',part1)