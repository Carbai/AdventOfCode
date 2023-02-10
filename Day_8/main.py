import numpy as np

with open('input.txt') as ifile:
    INPUT=[line.replace('\n', '') for line in ifile.readlines()]

for i in range(len(INPUT)):
    INPUT[i]=list(INPUT[i])

#PART ONE
visible_trees = len(INPUT)*4 - 4

def extract(lst):    ## swap rows and columns
    return list(list(zip(*lst)))

def is_tree_visible(i:int,j:int,tree:int,tree_cross:list)-> bool:

    if tree > max(tree_cross[i][:j]):  ## SEEN LEFT
        return True
    elif tree > max(tree_cross[i][j+1:]): ## SEEN RIGHT
        return True
    tree_cross = extract(tree_cross)
    if tree > max(tree_cross[j][:i]):  ## SEEN TOP
        return True
    elif tree > max(tree_cross[j][i+1:]): ## SEEN BOTTOM
        return True
    else:
        return

#PART TWO
def CheckForLess(list1, val):
    return(all(x < val for x in list1))

def find_pos_max(i:int, j:int, grid:list)->list:
    # top = 0
    # bottom = 0
    # left = 0
    # right = 0
    for k in reversed(range(j)):
        if int(grid[i][k]) >= int(grid[i][j]):
            left = j-k
            break
        elif CheckForLess(grid[i][:j], grid[i][j]):
            left = j
            break
    for k in range(j+1,len(grid[i])):
        if int(grid[i][k]) >= int(grid[i][j]):
            right = k-j 
            break
        elif CheckForLess(grid[i][j+1:], grid[i][j]):
            right = len(grid[i])-j-1
            break
    grid = extract(grid)
    for k in reversed(range(i)):
        if int(grid[j][k]) >= int(grid[j][i]):
            top = i-k
            break
        elif CheckForLess(grid[j][:i], grid[j][i]):
            top = i
            break
    for k in range(i+1,len(grid[j])):
        if int(grid[j][k]) >= int(grid[j][i]):
            bottom = k-i
            break
        elif CheckForLess(grid[j][i+1:], grid[j][i]):
            bottom = len(grid[j])-i-1
            break 
    return left*right*top*bottom

def parsing_line(tree_grid:list) -> list:
    new_trees=0
    part_two=[]
    tree_grid=list(tree_grid)
    for i in range(1,len(tree_grid)-1):
        for j in range(1,len(tree_grid[i])-1):
            if is_tree_visible(i,j,tree_grid[i][j],tree_grid):
                new_trees+=1
            part_two.append(find_pos_max(i,j,tree_grid))
    return new_trees, max(part_two)

tmp, result2=parsing_line(INPUT)
        
print('PART ONE', visible_trees+tmp)
print('PART TWO:', result2)