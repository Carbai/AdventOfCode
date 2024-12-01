from audioop import tomono
from curses.ascii import isdigit


with open ('input.txt') as ifile:
    INPUT = ifile.read()
    INPUT=INPUT.split('\n')
    

def find_folders(commands: list) -> tuple: # Return folders names
    return [commands[i].strip().replace('$ cd ', '') for i in range(len(commands)) if '$ cd' in commands[i]]

def folder_content(commands: list) -> tuple: # Return folder content
    test = False
    content_list=[]
    for content in commands:
        if '$ ls' in content: 
            
            test = False
            content_list.append([])
            index = len(content_list)-1
            
        elif '$ cd' in content:
            test = True
            
        else:
            if test == False:
                content_list[index] += [content]

    return (content_list)

def my_dict(input: list) -> dict:
    keys = find_folders(input)
    keys = [value for value in keys if value != '..']
    values = folder_content(INPUT)
    my_dict_build = {keys[i]: values[i] for i in range(len(keys))}
    return my_dict_build

class Tree:
    def __init__(self):
       # self.val = None
        self.parent = None
        self.children = None

def build_tree(input: list) -> Tree:
    tmp = my_dict(input)
    print(tmp['/'])
    
    for item in tmp:
        sum_t = 0
        tree = Tree()
        tree.children = tmp[item]

        count = sum('dir ' in s for s in tmp[item])
        while count != 0:
            for ele in tmp[item]: 

            
                if 'dir' in ele:
                    print(tmp[item],'OHOH')
                    tmp[item]+=substitute_key_value(tmp, ele)
                    tmp[item].remove(ele)
                    count = sum('dir ' in s for s in tmp[item])

        tmp[item] = sum_list_integers(tmp[item])
    
    return sum([val for val in tmp.values() if val < 100000])

def substitute_key_value(my_dict: dict, key: str) -> list:  
    real_key = key.replace('dir ', '')
    print(key, real_key, my_dict[real_key],'HERE')
    return my_dict[real_key]

def sum_list_integers(values: list) -> int:
    final = 0
    for item in values:
        final += sum([int(s) for s in item.split() if s.isdigit()])
    return final


print(build_tree(INPUT))
#print(my_dict(INPUT))