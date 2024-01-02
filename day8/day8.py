from pathlib import Path
from collections import defaultdict
import re
import math

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        # children=[]
        

    def insert (self ,data):
        if self.data:
            if data <self.data:
                if self.left is None:
                    self.left =Node(data)
                else:
                    self.left.insert(Node)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(Node)
            else :
                self.data =data
    
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()
        # print(self.data)

    def traverse(self):
        nodes_to_visit = [self]

        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.data)
            nodes_to_visit += nodes_to_visit.children
def Tree():
    return defaultdict(Tree)

def steps(cur):
    count = 0
    while cur[2] != 'Z':
        step = walk[count % len(walk)]
        if step == 'L':
            cur = children[cur][0]
        else:
            cur = children[cur][1]
        count += 1
    return count
    
    
    
    
    
    
    
if __name__ == "__main__":

    data = Path(__file__).with_name("input.txt").read_text().splitlines()
    walk = data[0]
    data = data[2:]
    children = defaultdict(str)
    for line in data:
         par, left, right = re.search("(...) = \((...), (...)\)", line).groups(0)
         children[par]=(left,right)
    # t = Tree()
    # for i ,val in enumerate(data):
    #     val = val.split('=')
    #     t[val[0]] = val[1]
    
    cur = [ n for n in children if n[2]== 'A']
    lens = [steps(node) for node in cur]
    print(lens)
    ans = math.lcm(*lens)
    print(ans)
    # cur='AAA'
    # str = 'ZZZ'
    # count = 0

    # while cur!= str:
    #     step = walk[count % len(walk)]
    #     if step == 'L':
    #         cur = children[cur][0]
    #     else:
    #         cur = children[cur][1]
    

    #     count += 1
        
    
    # print(count)
    

    # print(header ,tree)

    # tree = Node('AAA')
    # tree.insert('CCC')
    # tree.insert('BBB')
    # print(tree.PrintTree())

