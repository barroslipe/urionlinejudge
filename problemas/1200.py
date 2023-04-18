class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    
    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.search_add(value, self.root)

    def search_add(self, value, no_):
        if value < no_.key:
            if no_.left is None:
                no_.left = Node(value)
            else:
                self.search_add(value, no_.left)
        else:
            if no_.right is None:
                no_.right = Node(value)
            else:
                self.search_add(value, no_.right)
    
    def print_infixa(self, no_):
        if no_ is not None:
            self.print_infixa(no_.left)
            if self.first:
                print(no_.key, end='')
                self.first = not self.first
            else:
                print('', no_.key, end='')
            self.print_infixa(no_.right)
    
    def print_inordem(self, no_):
        if no_ is not None:
            if self.first:
                print(no_.key, end='')
                self.first = not self.first
            else:
                print('', no_.key, end='')
            self.print_inordem(no_.left)
            self.print_inordem(no_.right)
    
    def print_posordem(self, no_):
        if no_ is not None:
            self.print_posordem(no_.left)
            self.print_posordem(no_.right)
            if self.first:
                print(no_.key, end='')
                self.first = not self.first
            else:
                print('', no_.key, end='')

    def search(self, no_, value):
    
        if (no_ is None) or (value == no_.key):
            return no_
        elif value < no_.key:
            return self.search(no_.left, value)
        else:
            return self.search(no_.right, value)
        

tree = Tree()

while True:
    try:
        comandos = input().split()
    except EOFError:
        exit(0)

    if comandos[0] == 'I':
        tree.add(comandos[1])
    elif comandos[0] == 'P':
        if tree.search(tree.root, comandos[1]) is not None:
            print(comandos[1], 'existe')
        else:
            print(comandos[1], 'nao existe')
    elif comandos[0] == 'INFIXA':
        tree.first = True
        tree.print_infixa(tree.root)
        print()
    elif comandos[0] == 'PREFIXA':
        tree.first = True
        tree.print_inordem(tree.root)
        print()
    elif comandos[0] == 'POSFIXA':
        tree.first = True
        tree.print_posordem(tree.root)
        print()