import re
from functools import reduce
from operator import mul
import numpy as np
import sys

WIDTH,HEIGHT=101,103
#pos_arr=np.zeros((HEIGHT,WIDTH))
#print(pos_arr.shape)
np.set_printoptions(threshold=sys.maxsize)
np.set_printoptions(linewidth=np.inf)
with open('./Data/day14.txt') as ifile:
    lines=ifile.read().split()
    def parse_input(pos: list) -> dict:
        robots_pos={}
        for p in range(0,len(pos),2):
            robots_pos[p]=([re.findall(r'[\-]?\d+',pos[i]) for i in range(p,p+2)])
        return robots_pos
            
    def calc_pos(pv: list,t=100, width=11, height=7) -> int:
        xi, yi = int(pv[0][1]), int(pv[0][0])
        vx, vy = int(pv[1][1]), int(pv[1][0])
        xf = ((vx * t) + xi) % height
        yf = ((vy * t + yi)) % width
        return xf, yf
    
    def get_quadrant(pos: list, width=11, height=7) -> int:
        h=height//2
        if pos[0] >= 0 and pos[0] < height//2:
            if pos[1] >=0 and pos[1] < width//2:
                return 1
            elif pos[1]>width//2:
                return 2
        elif pos[0] > height//2:
            if pos[1] >=0 and pos[1] < width//2:
                return 3
            elif pos[1] > width//2:
                return 4
        return 
        


    robots_pos=parse_input(lines)
    xf=[]
    quadrants_count={k: 0 for k in range(1,5)}
  #  print(robots_pos)
    for time in range(100):
        pos_arr=np.zeros((HEIGHT,WIDTH))
        xf=[]
        print('TIME',time)
        for robot, pv in robots_pos.items():
            xf.append(calc_pos(pv,width=WIDTH,height=HEIGHT,t=time))
        xf_nodup=set([(i,xf.count(i)) for i in xf])
    for pos in xf_nodup:

        q=get_quadrant(pos[0],width=WIDTH,height=HEIGHT)
        if q:
            quadrants_count[q]+=pos[1]
        #Uncomment the following for part two
        # for pos in list(set(xf)):
        #         pos_arr[pos[0],pos[1]]=1
        # print(pos_arr)
    
    print('Solution to part one: ', reduce(mul,quadrants_count.values()))

