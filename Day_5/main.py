from functools import partialmethod
import numpy as np
import re
with open ('example.txt') as ifile:
    LINES=ifile.readlines()
    LINES=[line.strip("\n") for line in LINES]

def find_struc_and_moves (input: list) -> dict:
    my_dict = {}
    stacks_list = file_parsing(input)[0]
    keys = [lett for lett in stacks_list[-1] if lett.isdigit()]
    stacks_list = stacks_list[:-1]
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

    return my_dict

def file_parsing(input: list) -> tuple:
    splitting_index = input.index("")
   # moves_to_do = get_moves(moves)
    return input[0:splitting_index], input[splitting_index+1:] 

def get_moves(lines: list) -> list:
    moves = file_parsing(lines)[1]
    moves_to_do = []
    for move in moves:
        moves_to_do.append([s for s in re.findall(r'-?\d+\.?\d*', move)])        
    return moves_to_do

    #part one  
def part_one(lines: list) -> str:
    my_dict = find_struc_and_moves(lines)
    moves_to_do = get_moves(lines)
    for move in moves_to_do:
        my_dict[move[-1]].extend(reversed(my_dict[move[1]][-int(move[0]) :]))
        my_dict[move[1]] = my_dict[move[1]][: -int(move[0])]
    return (solution_str(my_dict))

    #part two
def part_two(lines: list) -> str:  
    my_dict = find_struc_and_moves(lines)
    moves_to_do = get_moves(lines)
    for move in moves_to_do:
        my_dict[move[-1]].extend(my_dict[move[1]][-int(move[0]) :])
        my_dict[move[1]] = my_dict[move[1]][: -int(move[0])]
    return solution_str(my_dict)

def solution_str(my_dict: dict) -> str: 
    return ''.join([val[-1] for val in my_dict.values()])
  
print('Part one solution:', part_one(LINES))
print('Part two solution:', part_two(LINES))