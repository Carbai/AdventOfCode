import numpy as np
import itertools
with open('./Data/day15.txt') as ifile:
    pos_map,moves=ifile.read().split('\n\n')
    pos_map=pos_map.split()
    
    def parse_input(pos, moves):
        doc={'boxes':[],'walls':[],'start':[],'moves':[]}
        for i in range(len(pos)):
            for j in range(len(pos[i])):
                if pos[i][j]=='#':
                    doc['walls'].append([i,j])
                elif pos[i][j]=='@':
                    doc['start'].append([i,j])
                elif pos[i][j]=='O':
                    doc['boxes'].append([i,j])
        for move in moves:
            if move=='^':
                doc['moves'].append([-1,0])
            elif move=='v':
                doc['moves'].append([1,0])
            elif move=='>':
                doc['moves'].append([0,1])
            elif move=='<':
                doc['moves'].append([0,-1])

        return doc

    def update_pos(curr_pos: dict, curr_move: list, curr_start: list) -> dict:
        move=True
        if curr_move[0] != 0:
            moving_boxes=[box for box in curr_pos['boxes'] if box[1]==curr_start[1]]
            poss_walls=[wall for wall in curr_pos['walls'] if wall[1]==curr_start[1]]
            if curr_move[0] > 0:
                moving_boxes=[box for box in curr_pos['boxes'] if box[1]==curr_start[1] and box[0]>curr_start[0]]
                poss_walls=[wall for wall in curr_pos['walls'] if wall[1]==curr_start[1] and wall[0]>curr_start[0]]
            else:
                moving_boxes=[box for box in curr_pos['boxes'] if box[1]==curr_start[1] and box[0]<curr_start[0]]
                poss_walls=[wall for wall in curr_pos['walls'] if wall[1]==curr_start[1] and wall[0]<curr_start[0]]
        if curr_move[1] != 0:
            if curr_move[1]==-1:
                moving_boxes=[box for box in curr_pos['boxes'] if box[0]==curr_start[0] and box[1]<curr_start[1]]
                poss_walls=[wall for wall in curr_pos['walls'] if wall[0]==curr_start[0] and wall[1]<curr_start[1]] 
            else:
                moving_boxes=[box for box in curr_pos['boxes'] if box[0]==curr_start[0] and box[1]>curr_start[1]]
                poss_walls=[wall for wall in curr_pos['walls'] if wall[0]==curr_start[0] and wall[1]>curr_start[1]] 
        if [curr_start[0]+curr_move[0],curr_start[1]+curr_move[1]] in poss_walls:
            return curr_pos
        elif [curr_start[0]+curr_move[0],curr_start[1]+curr_move[1]] in moving_boxes:

            boxes=[[curr_start[0]+curr_move[0],curr_start[1]+curr_move[1]]]
            while move:
                moving_boxes.remove(boxes[-1])
                if [boxes[-1][0]+curr_move[0],boxes[-1][1]+curr_move[1]] in poss_walls:
                    return curr_pos
                elif [boxes[-1][0]+curr_move[0],boxes[-1][1]+curr_move[1]] in moving_boxes:
                    boxes.append([boxes[-1][0]+curr_move[0],boxes[-1][1]+curr_move[1]])
                else:
                    curr_pos['boxes']=[[value[0]+curr_move[0],value[1]+curr_move[1]] if value in boxes else value for value in curr_pos['boxes']]
                    curr_start=[curr_start[0]+curr_move[0],curr_start[1]+curr_move[1]]
                    move=False
        else:
            curr_start=[curr_start[0]+curr_move[0],curr_start[1]+curr_move[1]]
        curr_pos['start']=[curr_start]
        return curr_pos

    doc=parse_input(pos_map,moves)
    moves_lst=doc['moves']
    for move in moves_lst:

        start=doc['start'][0]
        doc=update_pos(doc,move,start)
    print('Solution to day one: ', sum([100*box[0]+box[1] for box in doc['boxes']]))

    ##PART TWO
    def scale_map(map: dict) -> dict:
        map['boxes']=[[[i[0],i[1]+i[1]],[i[0],i[1]+i[1]+1]] for i in map['boxes']]
        map['walls']=[[[i[0],i[1]+i[1]],[i[0],i[1]+i[1]+1]] for i in map['walls']]
        map['start']=[[i[0],i[1]+i[1]] for i in map['start']]
        return map
    def p2(map: dict, curr_move: list, curr_start: list, i):
        boxes=map['boxes'].copy()
        walls=sum(map['walls'],[])
        moving_bxs=[]
        if [curr_start[0]+curr_move[0],curr_start[1]+curr_move[1]] in walls:
            return map
        elif [box for box in boxes if [curr_start[0]+curr_move[0],curr_start[1]+curr_move[1]] in box]:
            prev_n=0
            moving_bxs.extend([box for box in boxes if [curr_start[0]+curr_move[0],curr_start[1]+curr_move[1]] in box])
            n=len(moving_bxs)
            while prev_n!=n:
                prev_n=len(moving_bxs)
                for b in moving_bxs:
                    if [box for box in boxes if any([[bb[0]+curr_move[0],bb[1]+curr_move[1]] in box for bb in b])]:
                        k=[box for box in boxes if box[0] in [[bb[0]+curr_move[0],bb[1]+curr_move[1]] for bb in b]
                           or box[1] in [[bb[0]+curr_move[0],bb[1]+curr_move[1]] for bb in b]]
                        for i in k:
                            if i not in moving_bxs:
                                moving_bxs.append(i)
                            boxes.remove(i)
                    if [wall for wall in walls if any([bb[0]+curr_move[0],bb[1]+curr_move[1]]==wall for bb in b)]:
                        return map
                    n=len(moving_bxs)
            map['start']=[[curr_start[0]+curr_move[0],curr_start[1]+curr_move[1]]]
            new_pos=[]
            for box in moving_bxs:
                
                new_pos.append([[b[0]+curr_move[0],b[1]+curr_move[1]] for b in box])
            map['boxes']=[box for box in map['boxes'] if box not in moving_bxs]+new_pos
        else:
            map['start']=[[curr_start[0]+curr_move[0],curr_start[1]+curr_move[1]]]
        return map

   ##Part two   
    big_map=scale_map(parse_input(pos_map,moves))
    i = [i for i in range(0,11)]
    for j,move in enumerate(moves_lst):
        start=big_map['start'][0]
        big_map=p2(big_map,move,start,i=j)
    print('Solution to part two: ', sum([100*box[0][0]+box[0][1] for box in big_map['boxes']]))#big_map['boxes']])#big_map['boxes']]))
