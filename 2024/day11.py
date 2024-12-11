with open('./Data/day11.txt') as ifile:
    lines=[int(i) for i in ifile.read().split()]
    
    def update_val(stone_val: int):
        if stone_val==0:
            return [1]
        i=len(str(stone_val))
        if i%2==0:
            stone_val=[int(i) for i in [str(stone_val)[:i//2],str(stone_val)[i//2:]]]
            for n,x in enumerate(stone_val):
                if len(str(x))>1 and str(x)[0]==0:
                    new_val=int(str(x)[1::])
                    stone_val=stone_val[0:n]+[new_val]+stone_val[n+1::]
            return stone_val
        return [stone_val*2024]
    
    #PART TWO

    def get_res(lines: list, n:int) -> int:
        i=0
        value_occ={key: 1 for key in lines}
        while i<n:
            occ_lst=[]
            for key, occ in value_occ.items():
                new_val=update_val(key)
                occ_lst.extend([[i,occ] for i in new_val])
            value_occ = {}
            for key, value in occ_lst:
                if key in value_occ:
                    value_occ[key] += value
                else:
                    value_occ[key] = value
            i+=1
        return sum(value_occ.values())

    print('Solution to part one: ',get_res(lines,n=25))
    print('Solution to part two: ',get_res(lines,n=75))
    
    