import math
from heapq import heapify, heappush, heappop

with open('./Data/day16.txt') as ifile:
    race_map=ifile.read().split()
    
    def parse_input(inp: list) -> dict:
        race_map={}
        for i in range(len(inp)):
            for j in range(len(inp[i])):
                race_map[(i,j)]=inp[i][j]
        return race_map
    
    def get_neig(current: tuple, maze: dict):
        neig=[]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        move = {'South': [1, 0], 'West': [0, -1], 'East': [0, 1], 'North': [-1, 0]}
        current_dir=[val for key,val in move.items() if key==current[1]][0]
        for dx, dy in directions:
            pos = (current[0][0] + dx, current[0][1] + dy)
            if current_dir==[dx,dy]:
                pos_dir=current[1]
                try: 
                    if maze[pos]=='.' or maze[pos]=='E':
                        neig.append((pos,pos_dir))
                except:
                    continue
            elif [abs(dx+current_dir[0]),abs(dy+current_dir[1])]==[1,1]:
                pos_dir=[key for key, val in move.items() if val==[dx,dy]]
                try: 
                    if maze[pos]=='.' or maze[pos]=='E':
                        neig.append((pos, pos_dir[0]))
                except:
                    continue
            else:
                pass
        return neig

    def is_rotating(curr_node, parent):
        move = {'South': [1, 0], 'West': [0, -1], 'East': [0, 1], 'North': [-1, 0]}
        parent_pos=parent[0]
        parent_dir=move[parent[1]]#parent[1]
        step=[curr_node[0]-parent_pos[0],curr_node[1]-parent_pos[1]]
        curr_dir=[(k,val) for k,val in move.items() if val==step]
        return (curr_dir[0][0],parent_dir==step)

    def dijkstra(start: tuple, end: tuple, maze: dict) -> list:
        queue=[(0, (start[0],'East'))]
        prev={(start[0],'East'): None}
        distances={(k, dir): math.inf for k in maze.keys() for dir in ['East','West','North','South']}
        distances[(start[0],'East')]=0
        heapify(queue)
        while queue:
            cost, vertex=heappop(queue)
            neig=get_neig(vertex, maze)
            if vertex[0]==end[0]:
                break
            for n in neig:
                if n[1]==vertex[1]:
                    dist=distances[vertex]+1
                else:
                    dist=distances[vertex]+1001
                if dist < distances[n]:
                    distances[n]=dist
                    heappush(queue,(dist,n))
                    prev[n]=vertex 
                elif dist==distances[n]:
                    prev[n]=(prev[n],vertex)
        min_=min([distances[(end[0], dir)] for dir in ['North', 'South', 'East', 'West']])
        prev_n=[key for key, val in distances.items() if val<=min_ and val != math.inf]
        return min([distances[(end[0], dir)] for dir in ['North', 'South', 'East', 'West']]), prev, prev_n

    def tuple_length_case(t):
        if isinstance(t[0][0], tuple):
            return True
        return False
    
    def traverse(start: tuple, end: tuple, path: dict) -> list:
        start=(start[0],'East')
        end=[(end[0], 'North'),(end[0], 'South'),(end[0], 'West'),(end[0], 'East'),]
        visited=[]
        to_chk=[]
        for e in end:
            tmp=[]
            try:
                curr=path[e]
                tmp.append(curr)
                while curr!=start:
                    curr=path[curr]
                    tmp.append(curr)
                    if tuple_length_case(curr):
                        to_chk.extend(curr[1:])
                        curr=path[curr[0]]  
                        tmp.append(curr)     
            except:
                continue
            if tmp[-1]==start:
                visited.extend(tmp)
                visited.append(e)
        heapify(to_chk)
        while to_chk:
            tmp=[]
            curr=heappop(to_chk)
            while curr!=start:
                    curr=path[curr]
                    tmp.append(curr)
                    if tuple_length_case(curr):
                        to_chk.extend(curr[1:])
                        curr=path[curr[0]]  
                        tmp.append(curr)    
            if tmp[-1]==start:
                visited.extend(tmp)
        vis=[]
        for i in visited:
            if i not in vis:
                vis.append(i)
        return len(vis)

    race_map=parse_input(race_map)
    start=[k for k in race_map.keys() if race_map[k]=='S']
    end=[k for k in race_map.keys() if race_map[k]=='E']
    p1_score, paths, path_n= dijkstra(start, end, race_map)

    print('Solution to part one: ', p1_score)
    print('Solution to part two: ', traverse(start, end, paths))
    


