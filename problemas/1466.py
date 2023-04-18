
from typing import Deque


class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

class TreeBin:
    def __init__(self):
        self.root = None
    
    def add_node(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.caminhar_add(key, self.root)
    
    def caminhar_add(self, key, node):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self.caminhar_add(key, node.left)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self.caminhar_add(key, node.right)

    def print_bfs(self):

        fila = Deque()

        first  = True

        if self.root is not None:
            fila.append(self.root)
                     
        while  len(fila) > 0:
            temp = fila.popleft()
            
            if first:
                first = not first
                print(temp.key, end='')
            else:
                print('',temp.key, end='')

            if temp.left is not None:
                fila.append(temp.left)
            
            if temp.right is not None:
                fila.append(temp.right)


c = int(input())

for i in range(c):
    n = int(input())
    nos = list(map(int, input().split()))

    treeBin = TreeBin()
    for j in nos:
        treeBin.add_node(j)
    
    print(f'Case {i+1}:')
    treeBin.print_bfs()
    print()
    print()