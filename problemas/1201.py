

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

    def delete_node(self, key):
        self.root = self.caminhar_delete(key, self.root)

    def caminhar_delete(self, key, node):

        if node is None:
            return None
        else:
            if key == node.key:
                if node.right is None and node.left is None:
                    return None
                else:
                    if node.right is not None and node.left is not None:
                        tmp = node.left
                        while tmp.right is not None:
                            tmp = tmp.right

                        node.key = tmp.key
                        tmp.key = key
                        node.left = self.caminhar_delete(key, node.left)
                        return node
                    else:
                        if node.right is None:
                            return node.left
                        else:
                            return node.right
            else:
                if key < node.key:
                    node.left = self.caminhar_delete(key, node.left)
                elif key > node.key:
                    node.right = self.caminhar_delete(key, node.right)

                return node
            
    def search_node(self, key):
        if self.caminhar_search(key, self.root) is None:
            return False
        else:
            return True

    def caminhar_search(self, key, node):
        if node == None or key == node.key:
            return node
        elif key <  node.key:
            return self.caminhar_search(key, node.left)
        else:
            return self.caminhar_search(key, node.right)
    
    def print_infixa(self):
        saida =[]
        self.caminhar_infixa(self.root, saida)
        if len(saida) != 0:
            print(*saida, sep=' ')
        
    def caminhar_infixa(self, node, saida):
        if node != None:
            self.caminhar_infixa(node.left, saida)
            saida.append(node.key)
            self.caminhar_infixa(node.right, saida)

    def print_prefixa(self):
        saida =[]
        self.caminhar_prefixa(self.root, saida)
        if len(saida) != 0:
            print(*saida, sep=' ')
        
    def caminhar_prefixa(self, node, saida):
        if node != None:
            saida.append(node.key)

            self.caminhar_prefixa(node.left, saida)
            self.caminhar_prefixa(node.right, saida)

    def print_posfixa(self):
        saida =[]
        self.caminhar_posfixa(self.root, saida)
        if len(saida) != 0:
            print(*saida, sep=' ')
        
    def caminhar_posfixa(self, node, saida):
        if node != None:
            self.caminhar_posfixa(node.left, saida)
            self.caminhar_posfixa(node.right, saida)

            saida.append(node.key)

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

tree_bin = TreeBin()

while True:
    
    try:
        comandos = input().split()
    except EOFError:
        exit(0)

    if comandos[0] == 'I':
        tree_bin.add_node(int(comandos[1]))
    elif comandos[0] == 'P':
        resultado = tree_bin.search_node(int(comandos[1]))
        if resultado:
            print(int(comandos[1]), 'existe')
        else:
            print(int(comandos[1]), 'nao existe')

    elif comandos[0] == 'R':
        tree_bin.delete_node(int(comandos[1]))
    elif comandos[0] =='INFIXA':
        tree_bin.print_infixa()
    elif comandos[0] =='PREFIXA':
        tree_bin.print_prefixa()
    elif comandos[0] =='POSFIXA':
        tree_bin.print_posfixa()
    else:
        print('saca')