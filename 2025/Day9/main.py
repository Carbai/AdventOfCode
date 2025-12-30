from pathlib import Path
from functools import cache
with Path("input.txt").open() as f:
    lines =[tuple(map(int, line.split(',')))
         for line in f.read().splitlines()]

def calc_area(p1,p2):
    a=max(p1[0],p2[0])-min(p1[0],p2[0])+1
    b=max(p1[1],p2[1])-min(p1[1],p2[1])+1
    return a*b


@cache
def point_in_poly(x,y):
    inside=False


    for (x1,y1),(x2,y2) in zip(lines, lines[1:]+lines[:1]):
        if (x==x1==x2 and min(y1,y2)<=y<=max(y1,y2) or
            y==y1==y2 and min(x1,x2)<=x<=max(x1,x2)):
            return True
        if ((y1>y)!=(y2>y)) and (x<(x2-x1)*(y-y1)/(y2-y1)+x1):
            inside=not inside
    return inside
    
def edge_intersects_rect(x1,y1,x2,y2,rx1,ry1,rx2,ry2):
    if y1==y2:
        if ry1<y1<ry2:
            if max(x1,x2)>rx1 and min(x1,x2)<rx2:
                return True
    else:
        if rx1<x1<rx2:
            if max(y1,y2)>ry1 and min(y1,y2)<ry2:
                return True
    return False

def square_valid(x1,x2,y1,y2):
    x1,x2=sorted([x1,x2])
    y1,y2=sorted([y1,y2])
    for x,y in [(x1,y1),(x1,y2),(x2,y1),(x2,y2)]:
        if not point_in_poly(x,y):
            return False
    for (ex1,ey1),(ex2,ey2) in zip(lines, lines[1:]+lines[:1]):
        if edge_intersects_rect(ex1,ey1,ex2,ey2,x1,y1,x2,y2):
            return False
    return True

area=0
part2=0
for i,p1 in enumerate(lines[:-1]):
    for j,p2 in enumerate(lines[1:]):
        curr_area=calc_area(p1,p2)
        area=max(curr_area,area)
        if curr_area>part2 and square_valid(p1[0],p2[0],p1[1],p2[1]):
            part2=curr_area


print(area)
print(part2)
