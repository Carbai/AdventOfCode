with open('./Data/day10.txt') as ifile:
    lines=ifile.read().split()
    rows=len(lines)
    cols=len(lines[0])
    def parse_input(inp: list) -> dict:
        map_dict={key:[] for key in range(10)}
        for n,line in enumerate(lines):
            line=[int(i) for i in line]
            for j in range(len(line)):
                map_dict[line[j]].append([n,j])
        return map_dict
    
    def get_moves(coord: list, rows, cols)-> list:
        moves=[[0,1],[0,-1],[1,0],[-1,0]]
        return [i for i in [[x+y for x,y in zip(coord, move)] for move in moves] if i[0]>=0 and i[0]<=rows and i[1]>=0 and i[1]<=cols]

    def get_trail(my_dict:dict, move:list, i:int, visited:list, rows: int, cols: int, flag='p1')->bool:
        n_trail=0
        if flag=='p1':
            if move in visited:
                return n_trail
            visited.append(move)
        if i == 9:
            return 1
        for m in get_moves(move, rows, cols):
            if m in my_dict[i+1]:
                n_trail+=get_trail(my_dict,m,i+1,visited,rows,cols,flag=flag)
        return n_trail
    
    def get_n_trails(inp: dict, rows: int, cols: int, flag='p1')->int:
        i=0
        res=0
        head=inp[0][0]
        for head in inp[0]:
          res+=get_trail(inp,head,i,[],rows,cols,flag=flag)     
        return res
    

    map_dict=parse_input(lines)
    print('Solution to part one: ', get_n_trails(map_dict,rows,cols,flag='p1'))

    print('Solution to part two: ', get_n_trails(map_dict,rows,cols,flag='p2'))
