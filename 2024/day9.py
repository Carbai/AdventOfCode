
from itertools import groupby

with open('./Data/day9.txt') as ifile:
    lines=[int(i) for i in ifile.read()]

    def parse_input(lines:list) -> dict:
        count_k=0
        vals=[]
        for n,line in enumerate(lines):
            if n%2==0:
                vals.extend([count_k]*line)
                count_k+=1
            else:
                vals.extend(['.']*line)
        return {key:val for key,val in zip(range(sum(lines)),vals)}

    def get_space_ndx(my_dict:dict) -> list:
        return [key for key,val in my_dict.items() if val=='.']

    def get_line(my_dict:dict) -> list:
        return [val for key,val in my_dict.items()]

    def get_p1_line(my_dict: dict) -> list:
        s_no_space=[i for i in get_line(data_dict) if i != '.']
        free_space,full_line=get_space_ndx(data_dict),get_line(data_dict)
        s_no_space_rev=[i for i in reversed(s_no_space[len(s_no_space)-len(free_space):len(s_no_space)])]
        for ndx, val in zip(free_space,s_no_space_rev):
            full_line[ndx]=val
        return full_line[0:len(get_line(my_dict))-len(free_space)]

    def get_res(my_lst:list) -> int:
        return sum([n*val for n, val in enumerate(my_lst) if val != '.'])

    data_dict=parse_input(lines)

    print('Solution to part one: ', get_res(get_p1_line(data_dict)))

    #PART TWO

    def get_int_ndx(my_dict:dict) -> list:
        ndxs=[k for k, g in groupby(get_space_ndx(data_dict))]
        return [ndxs[0]]+[ndxs[i+1] for i, ndx in enumerate(ndxs[0:len(ndxs)-1]) if ndxs[i+1]!=ndx+1]
 
    def get_int_info(my_dict:dict) -> list:
        lst1=[sum(1 for _ in group) for _, group in groupby(get_line(data_dict))]
        lst2=[k for k, g in groupby(get_line(data_dict))]
        return [list(i) for i in [(val1,val2) for val1,val2 in zip(get_int_ndx(data_dict),[val1 for val1,val2 in zip(lst1,lst2) if val2=='.'])]]
        
    def get_start_ndx(my_dict,lst):
        n_ndx=[key for key, value in my_dict.items() if value != '.']
        for val1 in n_ndx:
            for j in range(val1+1,val1 + lst[0]):
                try:
                    n_ndx.remove(j)
                except ValueError:
                    pass
            lst=lst[1::]
        return n_ndx
            
    def get_p2_line(my_dict: dict, values_ndx: tuple) -> list:
        ori_line=get_line(data_dict)
        full_line=[sum(1 for _ in group) for _, group in groupby(get_line(data_dict)) if _ != '.']
        n_ndx=get_start_ndx(my_dict,full_line)
        for i in reversed(range(len(full_line))):
            for j in range(len(values_ndx)):
                if values_ndx[j][1]>=full_line[i] and n_ndx[i]>values_ndx[j][0]:
                    ori_line[values_ndx[j][0]:values_ndx[j][0]+full_line[i]]=ori_line[n_ndx[i]:n_ndx[i]+full_line[i]]
                    
                    ori_line[n_ndx[i]:n_ndx[i]+full_line[i]]=['.']*full_line[i]
                    if values_ndx[j][1]-full_line[i]>0:
                        values_ndx[j][0]+=full_line[i]
                        values_ndx[j][1]-=full_line[i]
                    else:
                        values_ndx.remove(values_ndx[j])
                    break
        return ori_line
    
    print('Solution to part two: ',get_res(get_p2_line(data_dict,get_int_info(data_dict))))




