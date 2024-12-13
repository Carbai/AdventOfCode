with open('./Data/day13.txt') as ifile:
    lines=ifile.read().split()
    data=[]
    for line in lines:
        for val in line:
            if val=='X' or val=='Y':
                data.append(int(line.replace(',','').split('+')[-1].split('=')[-1]))
                break
    machines={i: [(data[i],data[i+1]),(data[i+2],data[i+3]),(data[i+4],data[i+5])] for i in range(0,len(data),6)}
    
    def calc_tokens(beh: list, flag: str):
        x1,y1=beh[0][0],beh[0][1]
        x2,y2=beh[1][0],beh[1][1]
        if flag=='p1':
            x,y=beh[2][0],beh[2][1]
        else:
            x,y=beh[2][0]+10000000000000,beh[2][1]+10000000000000
        a=round((x-(y*x2/y2))/(x1-(y1*x2/y2)),3)
        b=round((y-(a*y1))/y2,3)
        if a.is_integer() and b.is_integer():
            return int(3*a+b)
        return 0

    tokens_p1=0
    tokens_p2=0
    
    for mach, behav in machines.items():
        tokens_p1+=calc_tokens(behav, flag='p1')
        tokens_p2+=calc_tokens(behav, flag='p2')
        
    print('Solution to part one: ', tokens_p1)
    print('Solution to part two: ', tokens_p2)