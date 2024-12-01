with open('./Data/day1_part1.txt') as ifile:
    lines=ifile.read().split()
    left=[int(lines[0])]
    right=[]
    for i in range(1,len(lines)):
        if i%2==0:
            left.append(int(lines[i]))
        else:
            right.append(int(lines[i]))
    left=sorted(left)
    right=sorted(right)

    def part_one(ids_left, ids_right):
        paired=[list(i) for i in zip(ids_left,ids_right)]
        res=[]
        for i in paired:
            res.append(abs(i[0]-i[1]))
        return sum(res)
    
    def part_two(ids_left, ids_right):
        res=[]
        for val in ids_left:
            res.append(ids_right.count(val)*val)
        return sum(res)

        
    print('Total distance: ', part_one(left,right))
    print('Similarity score: ', part_two(left,right))
