import itertools
from itertools import product
import time
start_time = time.time()

with open('./Data/day7.txt') as ifile:
    ops_dict={}
    lines = ifile.read().split('\n')
    for line in lines:
        if int(line.split(':')[0]) in ops_dict.keys():
                ops_dict[(line.split(':')[0])+'_'+line.split(':')[1]]=[int(i) for i in line.split(':')[1].split()]
        else: 
            ops_dict[int(line.split(':')[0])]=[int(i) for i in line.split(':')[1].split()]
    
    def get_comb(n,ops=['* ','+ ','|| '],flag='p1'):
        if flag=='p1':
            ops=['* ','+ ']
        combinations_list = list(product(ops, repeat=n-1))
        combinations_strings = list(map(lambda comb: ''.join(comb), combinations_list))
        return [i.split() for i in combinations_strings]
    
    def get_val(ops,values):
        curr_val=values[0]
        for j in range(1,len(values)):
            if ops[j-1]=='*':
                curr_val*=values[j]
            elif ops[j-1]=='+':
                curr_val+=values[j]
            else:
                curr_val=int(str(curr_val)+str(values[j]))
        return curr_val

    targets=ops_dict.keys()
    values=ops_dict.values()
    keep=[]
    discard=[]

    for target, val in zip(targets,values):
        local_keep=[]
        combs=get_comb(len(val),flag='p1')
        ori_target=target
        if type(target)==str:
            target=int(target.split('_')[0])
        for comb in combs:
            if target==get_val(comb,val):
                local_keep.append(target)
        if local_keep:
            keep.extend(list(set(local_keep)))
        else:
            discard.append(ori_target)
            
    p1=sum(keep)
    print('Solution to part one: ', sum(keep))

    ##Part two 
    keep=[]
    for target, val in zip(targets,values):
        local_keep=[]
        ori_target=target
        combs=get_comb(len(val),flag='p2')
       # print(combs)
        if ori_target in discard:
            if type(target)==str:
                target=int(target.split('_')[0])
            for comb in combs:
                if '||' in comb:
                    if target==get_val(comb,val):
                        local_keep.append(target)
            if local_keep:
                keep.extend(list(set(local_keep)))

    print('Solution to part two: ', sum(keep)+p1)
    print("--- %s seconds ---" % (time.time() - start_time))


