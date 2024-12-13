with open('./Data/day12.txt') as ifile:
    lines=ifile.read().split()
    def parse_inp(inp: list) -> dict:
        plants_map={}
        for i in range(len(inp)):
            for j in range(len(inp[i])):
                try:
                    plants_map[inp[i][j]].append([i,j])
                except KeyError:
                    plants_map[inp[i][j]]=[[i,j]]
        return plants_map
    plants_map=parse_inp(lines)
    
    def is_in_region(pos,regions) -> bool:
        moves=[[0,1],[0,-1],[1,0],[-1,0]]
        pos=[[pos[0] + move[0], pos[1] + move[1]] for move in moves]
        return any(i in regions for i in pos)
    
    def eval_r(pos: list) -> list:
        region=[pos[0]]
        pos=pos[1::]
        remaining_pos=pos.copy()
        region_prev=[]
        while len(region)!= len(region_prev):
            region_prev=region.copy()
            for i in pos:
                if is_in_region(i,region):
                    region.append(i)
                    remaining_pos.remove(i)
            pos=remaining_pos
        return region,remaining_pos 

    def get_r2(pos: list,plant) -> list:
        regions=[]
        while pos:
            region,pos=eval_r(pos)
            regions.append(region)
        return regions

    regions={}
    for plant, pos in plants_map.items():
        regions[plant]= get_r2(pos,plant)

    def update_p(region: list) -> int:
        moves=[[0,1],[1,0],[-1,0],[0,-1]]
        p=0
        for point in region:
            neigs=[[point[0] + move[0], point[1] + move[1]] for move in moves]
            p+=(4-sum(1 for neig in neigs if neig in region))
        return p
    
    def is_adj(sides: list, current: list, flag: str) -> bool:
        if flag=='row_':
            dist=[[current[0]-side[0],current[1]-current[1]] for side in sides]
            return [0,0] 

    def update_p_p2(region: list, plant) -> int:
        p=0
        min_r,max_r=[min(x[0] for x in region),max(x[0] for x in region)]
        min_c,max_c=[min(x[1] for x in region),max(x[1] for x in region)]
        prev_up=None
        prev_down=None
        if min_r==max_r:
            p+=2
        else:  
            for i in range(min_r,max_r+1):
                for j in range(min_c,max_c+1):
                    if [i,j] in region:
                        try:
                            if not [i+1,j] in region and prev_down==[i,j-1]:
                               prev_down=[i,j]
                            elif not [i+1,j] in region and prev_down!=[i,j-1]:
                                p+=1
                                prev_down=[i,j]
                        except IndexError:
                            continue
                        try:
                            if not [i-1,j] in region and prev_up==[i,j-1]:
                                prev_up=[i,j]
                            elif not [i-1,j] in region and prev_up!=[i,j-1]:
                                p+=1
                                prev_up=[i,j]
                        except IndexError:
                            pass
        prev_left=None
        prev_right=None
        if min_c==max_c:
            p+=2
        else:
            for j in range(min_c,max_c+1):
                for i in range(min_r,max_r+1):
                    if [i,j] in region:
                        try:
                            if not [i,j-1] in region and prev_right==[i-1,j]:
                                prev_right=[i,j]
                            elif not [i,j-1] in region and prev_right!=[i-1,j]:
                                p+=1
                                prev_right=[i,j]
                        except IndexError:
                            continue
                        try:
                            if not [i,j+1] in region and prev_left==[i-1,j]:
                                prev_left=[i,j]

                            elif not [i,j+1] in region and prev_left!=[i-1,j]:
                                    p+=1
                                    prev_left=[i,j]
                                
                        except IndexError:
                            continue
        return p

    price_p1=0
    price_p2=0
    for plant, reg in regions.items():  
        for r in reg:
            price_p1+=update_p(r)*len(r)
            price_p2+=update_p_p2(r,plant)*len(r)
    print('Solution to part one: ', price_p1)
    print('Solution to part two: ', price_p2)
                
