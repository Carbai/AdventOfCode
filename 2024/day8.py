from itertools import product

with open('./Data/day8.txt') as ifile:
    lines=ifile.read().split('\n')

    def get_map(inp):
        map_dict={'all_pos':[]}
        for n,line in enumerate(inp):
            for i in range(len(line)):
                if line[i]!='.':
                    try:
                        map_dict[line[i]].append([n,i])
                    except KeyError:
                        map_dict[line[i]]=[[n,i]]
                map_dict['all_pos'].append([n,i])
        return map_dict
    
    def get_dist(f1,f2):
        return [f2[0]-f1[0],f2[1]-f1[1]]
    
    def calc_antinodes(f1,f2,d):
        if f1[0]==f2[0]:
            return [[f1[0],min(f1[1],f2[1])-d[1]],[f1[0],min(f1[1],f2[1])+d[1]]]
        else:
            min_lst = f1 if f1[0] < f2[0] else f2
            max_lst = f1 if f1[0] > f2[0] else f2
            return [[x-y for x,y in zip(min_lst,d)],[x+y for x,y in zip(max_lst,d)]]

    def get_valid_antinodes(map_pos,antinodes_pos):
        return [pos for pos in antinodes_pos if pos in map_pos]
    
    map_dict=get_map(lines)
    map_dict['antinodes']=[]
    for key, value in map_dict.items():
        if key != 'antinodes' and key!='all_pos':
            antinodes_pos=[]

            for i in range(len(value)-1):

                tmp_antinodes=[]
                for j in range(i+1,len(value)):
                    
                    dist=get_dist(value[i],value[j])
                    tmp_antinodes.extend(calc_antinodes(value[i],value[j],dist))
                valid_antinodes=get_valid_antinodes(map_dict['all_pos'],tmp_antinodes)
                if valid_antinodes:
                    map_dict['antinodes'].extend(valid_antinodes)
                
    print('Solution to part one: ', len(list(set(tuple(pos) for pos in map_dict['antinodes']))))

    ## Part two
    map_dict['antinodes']=[]
    for key, value in map_dict.items():
        if key != 'antinodes' and key!='all_pos':
            antinodes_pos=[]
            valid_antinodes=[]

          #  print('START',key,value)
            for i in range(len(value)-1):
                
                tmp_antinodes=[]

                antinodes_pos=[]
                for j in range(i+1,len(value)):
                    
                    dist=get_dist(value[i],value[j])
                    poss=calc_antinodes(value[i],value[j],dist)
                    tmp_antinodes.extend(calc_antinodes(value[i],value[j],dist))
                    valid_antinodes=get_valid_antinodes(map_dict['all_pos'],tmp_antinodes)

                    val1,val2=poss[0],poss[1]
                    if valid_antinodes:

                        map_dict['antinodes'].extend(valid_antinodes)
                        while sorted(valid_antinodes) != sorted(antinodes_pos) and len(valid_antinodes)!=len(antinodes_pos):
                            antinodes_pos.extend(valid_antinodes)

                            antinodes_pos=list(set(tuple(pos) for pos in antinodes_pos))
                            
                            val1=[x-y for x,y in zip(val1,dist)]
                            val2=[x+y for x,y in zip(val2,dist)]
                            if val1[0]>=0 and val1[1]>=0:
                                tmp_antinodes.append(val1)
                            if val2[0]>=0 and val2[1]>=0:
                                tmp_antinodes.append(val2)
                            valid_antinodes.extend(get_valid_antinodes(map_dict['all_pos'],tmp_antinodes))
                            valid_antinodes=list(set(tuple(pos) for pos in valid_antinodes))
                            valid_antinodes = [list(t) for t in valid_antinodes]
                            antinodes_pos = [list(t) for t in antinodes_pos]
                        map_dict['antinodes'].extend(valid_antinodes)
n=0
for key, value in map_dict.items():
    if key != 'antinodes' and key!='all_pos':
        map_dict['antinodes'].extend(value)

print('Solution to part one: ', len(list(set(tuple(pos) for pos in map_dict['antinodes'])))+n)
                