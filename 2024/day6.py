with open('./Data/day6.txt') as ifile:
    lines=ifile.read().strip('\n').split()
    map_dict={'obstacles':[],'head':[],'end':[],'all_pos':[],'ord_pos':[]}
    map_dict['end'].extend([[0, j] for j in range(len(lines[0]))])  # Top border
    map_dict['end'].extend([[i, 0] for i in range(1,len(lines))])    # Left border
    map_dict['end'].extend([[len(lines)-1, j] for j in range(1,len(lines[0]))])  #Bottom border
    map_dict['end'].extend([[i,len(lines[0])-1] for i in range(1,len(lines)-1)])    # Right border

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j]=='^':
                map_dict['head'].append([i,j])
            elif lines[i][j]=='#':
                map_dict['obstacles'].append([i,j])

    def move_guard(curr_pos, obst_pos, flag):
        try:
            if flag=='up':
                close_obs=max(i for i in obst_pos if (i[1]==curr_pos[1] and i[0]<curr_pos[0]))
                return [close_obs[0]+1,curr_pos[1]]
            if flag=='right':
                close_obs=min(i for i in obst_pos if (i[0]==curr_pos[0] and i[1]>curr_pos[1]))
                return [curr_pos[0],close_obs[1]-1]
            if flag=='left':
                close_obs=max(i for i in obst_pos if (i[0]==curr_pos[0] and i[1]<curr_pos[1]))
                return [curr_pos[0],close_obs[1]+1]
            if flag=='down':
                close_obs=min(i for i in obst_pos if (i[1]==curr_pos[1] and i[0]>curr_pos[0]))
                return [close_obs[0]-1,curr_pos[1]]
        except ValueError:
            return None
        
        
    def is_end(curr_pos, ends):
        return curr_pos in ends
    
    def get_directions(flag):
        flags_dict={'up':'right','right':'down','down':'left','left':'up'}
        return flags_dict[flag]
    
    def get_end(curr_pos, ends, flag):
        if flag=='up':
            close_end=[i for i in ends if i[1]==curr_pos[1] and i[0]<curr_pos[0]]
            return close_end
        if flag=='right':
            close_end=[i for i in ends if i[0]==curr_pos[0] and i[1]>curr_pos[1]]
            return close_end
        if flag=='left':
            close_end=[i for i in ends if i[0]==curr_pos[0] and i[1]<curr_pos[1]]
            return close_end
        if flag=='down':
            close_end=[i for i in ends if i[1]==curr_pos[1] and i[0]>curr_pos[0]]
            return close_end
        return
    
    flag='up'
    curr_pos=map_dict['head'][-1]

    while not is_end(curr_pos, map_dict['end']):
        if move_guard(curr_pos,map_dict['obstacles'],flag):
            map_dict['head'].append(move_guard(curr_pos,map_dict['obstacles'],flag))
            flag=get_directions(flag)
        else:
            map_dict['head'].extend(get_end(curr_pos,map_dict['end'],flag))
        curr_pos=map_dict['head'][-1]
    def get_all_points(pos1,pos2):
        if pos1[0]==pos2[0]:
            if pos1[1]>pos2[1]:
                return [[pos1[0],j] for j in reversed(range(pos2[1]+1,pos1[1]))]
            else:
                return [[pos1[0],j] for j in range(pos1[1]+1,pos2[1])]
        else:
            if pos1[0]>pos2[0]:
                return [[j, pos1[1]] for j in reversed(range(pos2[0]+1,pos1[0]))]  
            else:
                return [[j,pos1[1]] for j in range(pos1[0]+1,pos2[0])]
    
    new_list=[map_dict['head'][0]]
    for i in range(len(map_dict['head'])-1):
        new_list.extend(get_all_points(map_dict['head'][i],map_dict['head'][i+1]))
        new_list.append(map_dict['head'][i+1])
        map_dict['head'].extend(get_all_points(map_dict['head'][i],map_dict['head'][i+1]))
    
    map_dict['ord_pos']=new_list
    print('Solution to part one: ', len(set(tuple(pos) for pos in map_dict['head'])))

    ##Part two
    map_dict['all_pos'].extend([i,j] for i in range(len(lines)) for j in range(len(lines[0])))
    n_loops=0
    curr_pos=map_dict['head'][0]
    
    flag='up'
    prev_flag=None
    next_pos=None
    loops=[]
    
    for i in map_dict['ord_pos'][1:]:
        curr_pos=map_dict['head'][0]

        positions={str(curr_pos):None}
        flag='up'
        map_dict['obstacles'].append(i)
        while not is_end(curr_pos, map_dict['end']):

            if move_guard(curr_pos,map_dict['obstacles'],flag):
                next_pos=move_guard(curr_pos,map_dict['obstacles'],flag)
                try:
                    if positions[str(next_pos)]==flag:
                        loops.append((str(i),flag))
                        break
                except KeyError:
                    positions[str(next_pos)]=flag
                flag=get_directions(flag)
                curr_pos=next_pos
            else:
                curr_pos=get_end(curr_pos,map_dict['end'],flag)[0]

        map_dict['obstacles'].remove(i)

    print('Solution to part two: ', len(set(loops)))
