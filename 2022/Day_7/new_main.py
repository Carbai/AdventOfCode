from struct import calcsize
from numpy import size


with open ('input.txt') as ifile:
    INPUT = ifile.read().split('\n')


class Node:
    def __init__(self, name, parent = None, size = 0):
      self.parent = parent
      self.children = []
      self.size = size
      self.name = name
   
    # def calcsize(self):
    #     for child in self.children:
    #         self.size += child.size

    def __repr__(self):
      return f"node data: {self.name}, children: {self.children}, size: {self.size}"

    # def add_children(self, children_list):
    #     for child in children_list:
    #         self.children.append(Node(name=child, parent=self.name))
        
def input_parser(input:list) -> Node:
    
    tree = Node("root")
    current_folder = tree
    for line in input[1:]:
        if "$ cd .." in line:
            current_folder = current_folder.parent
        elif "$ ls" in line:
            pass
        elif "$ cd" in line and "/" not in line:
            name_tmp = line.split(" ")[-1]
            current_folder = [child for child in current_folder.children if child.name == name_tmp][0]          
        else:
            if line.split(" ")[0].isdigit() == True:
                current_folder.children.append(Node(name = line.split(" ")[-1], parent=current_folder, size= int(line.split(" ")[0])))
            else:
                current_folder.children.append(Node(name = line.split(" ")[-1], parent=current_folder))
    return tree

def calc_size(tree: Node,list_size=[]) -> None:
    for child in tree.children:
        if child.size == 0:
            calc_size(child)
        tree.size += child.size
    return tree
    if tree.size < 100000:
        list_size.append(tree.size)
    
    return sum(list_size)

def part_two(tree: Node,list_size=[]) -> None:
    for child in tree.children:
        if child.size == 0:
            part_two(child)
        tree.size += child.size
    list_size.append(tree.size)
 #   unused_space = 70000000 - list_size[-1] 
    unused_space = 70000000 - tree.size
    to_free = 30000000 - unused_space
    return min(list_size, key=lambda x:abs(x-to_free))
   # return tree.size, unused_space, list_size
    #for item in list_size:
   # return min(list_size, key=lambda x:abs(x-unused_space))
  #  return unused_space
      #  list_size.append(tree.size)

      #  return tree

#def get_big_dirs(tree: Node) -> None:

# print(input_parser(INPUT))

my_tree=input_parser(INPUT)

#print(calc_size(my_tree))
print(part_two(my_tree))
