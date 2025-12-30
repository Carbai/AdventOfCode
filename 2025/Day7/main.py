from pathlib import Path

with Path('input7.txt').open() as f:
    lines=[line.replace('\n','') for line in f.readlines()]
#print('lines',lines)
size=len(lines)
#print(size)
inp={(i,j): l for i, line in enumerate(lines) for j, l in enumerate(line)}
def part_one(inp):
    stack=[key for key in inp.keys() if inp[key]=='S']
    n_split=0
    nodes=[]
    #print(inp)
    timelines=0
    while stack:
        pos=stack.pop()
        new_pos=(pos[0]+1,pos[1])
        nodes.append(pos)
        if new_pos[0]==size-1:
            timelines+=1
            print('update', timelines)
        if new_pos not in inp.keys() or new_pos in nodes:
            continue
        if inp[new_pos]=='.':
            stack.append(new_pos)
        else:
            n_split+=1
            new_pos=[(pos[0]+1,pos[1]-1),(pos[0]+1,pos[1]+1)]
            new_pos=[p for p in new_pos if p in inp.keys()]
            stack.extend(new_pos)
    return n_split
assert part_one(inp) == 1667

def part_two(inp):
    memo = {}
    stack = []
    for key in inp:
        if inp[key] == 'S':
            stack.append((key, False))  

    n_paths = 0

    while stack:
        pos, done = stack.pop()
        if pos[0] >= size:
            memo[pos] = 1
            continue

        if done:
            total = 0
            if inp[pos] == '^':
                total += memo[(pos[0] + 2, pos[1] + 1)]
                total += memo[(pos[0] + 2, pos[1] - 1)]
            else:
                total += memo[(pos[0] + 2, pos[1])]

            memo[pos] = total
            continue
        if pos in memo:
            continue
        stack.append((pos, True))
        if inp[pos] == '^':
            stack.append(((pos[0] + 2, pos[1] + 1), False))
            stack.append(((pos[0] + 2, pos[1] - 1), False))
        else:
            stack.append(((pos[0] + 2, pos[1]), False))

    start=[key for key in inp.keys() if inp[key]=='S']
    return memo[start[0]]

        
print('Part two solution:', part_two(inp))


