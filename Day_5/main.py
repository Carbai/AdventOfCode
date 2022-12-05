import numpy as np
import re
with open ('example.txt') as ifile:
    LINES=ifile.readlines()
    LINES=[line.strip("\n") for line in LINES]

def find_struc_and_moves (input: list) -> list:
    my_dict = {}
    splitting_index = input.index("")
    stacks_list = input[0:splitting_index]
    keys = [lett for lett in stacks_list[-1] if lett.isdigit()]
    stacks_list = input[0:splitting_index-1]
    stacks_list = [ele.replace("[", " ").replace("]", " ") for ele in stacks_list]
    
    values = list(map(list, zip(*stacks_list)))

    for i in reversed(range(len(values))):
            
        if all(x == " " for x in values[i]):
            values.remove(values[i])

    [value.reverse() for value in values]
    new_values = []
    for value in values:
        new_values.append([x for x in value if x != ' '])

    my_dict={k:v for k,v in zip(keys,new_values)}

    moves = input[splitting_index+1:]
    moves_to_do = get_moves(moves)

    for move in moves_to_do:
        for ele_to_move in range(move[0]):
         #   print(ele_to_move)
            #part one
            to_append=my_dict.get(str(move[1]))[-1]

            #part two
       # to_append=my_dict.get(str(move[1]))[len(my_dict.get(str(move[1])))-1-move[0] :]

       # my_dict[str(move[-1])].append(to_append)
       # my_dict[str(move[1])].remove(to_append)
            #(len(my_dict.get(str(move[1])))-1-ele_to_move)
       # print(to_append)
            #my_dict[str(move[1])],my_dict[str(move[1])].pop(0))

           # print(to_append[len(to_append)-1], 'toapp')
            #[len(my_dict.get(str(move[1])))-ele_to_move]
         #   print(my_dict.get(str(move[1])),type(ele_to_move), len(my_dict.get(str(move[1])))-ele_to_move)
            my_dict[str(move[-1])].append(to_append)
            #my_dict[str(move[1])].pop(my_dict.get(str(move[1]))[len(my_dict.get(str(move[1])))-1-ele_to_move])
          #  my_dict[str(move(1))]=my_dict[str(move(1))].values()[:,len(my_dict.get(str(move[1])))-1-move[0]]
          #  print([my_dict[str(move[1])].values()])
          #  print(type(my_dict.get(str(move[1]))[len(my_dict.get(str(move[1])))-1-ele_to_move]), 'look')
           
            #part one
            my_dict[str(move[1])].pop()
       
    
    res = [val[-1] for val in my_dict.values()]
    return ''.join(res)
  #  return my_dict



def get_moves(move_str: list) -> list:
    moves_list = []
    for move in move_str:
        moves_list.append([int(s) for s in re.findall(r'-?\d+\.?\d*', move)])        
    return moves_list

print(find_struc_and_moves(LINES))