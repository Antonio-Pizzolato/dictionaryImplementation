class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        new_node = Node(key, value)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    if current_node.left is None:
                        current_node.left = new_node
                        new_node.parent = current_node
                        break
                    else:
                        current_node = current_node.left
                else:  # è l'else che comprende i valori maggiori del nodo considerato, inoltre se due valori sono uguali viene messo comunque a destra
                    if value == current_node.value:
                        if current_node.right is None:
                            current_node.right = new_node
                            new_node.parent = current_node
                            break
                        else:
                            current_node = current_node.right
                    else:
                        if current_node.right is None:
                            current_node.right = new_node
                            new_node.parent = current_node
                            break
                        else:
                            current_node = current_node.right

    def search(self, value):  # versione iterativa più veloce della ricorsiva
        current_node = self.root
        while current_node is not None:
            if value == current_node.value:
                print("Key:", current_node.key, "Value:", current_node.value)
                return current_node
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return print("Errore: Valore non trovato")  # non ritornando None potrebbe dare un errore nella cancellazione

    def minimum(self, node):
        while node.right is not None:
            node = node.right
        return node

    def successor(self, node):
        if node.right is not None:
            return self.minimum(node.right)
        parent = node.p
        while parent is not None and node == parent.right:
            node = parent
            parent = parent.p
        return parent

    def transplant(self, node1, node2):
        if node1.p is None:
            self.root = node2
        elif node1 == node1.p.left:
            node1.p.left = node2
        else:
            node1.right = node2
        if node2 is not None:
            node2.p = node1.p

    def delete(self, value):
        node_to_delete = self.search(value)

        if node_to_delete is None:
            return

        if node_to_delete.left is None:
            self.transplant(node_to_delete, node_to_delete.left)
        elif node_to_delete.right is None:
            self.transplant(node_to_delete, node_to_delete.right)
        else:
            successor = self.minimum(node_to_delete.right)
            if successor.p != node_to_delete:
                self.transplant(successor, successor.right)
                successor.right = node_to_delete.right
                successor.right.p = successor
            self.transplant(node_to_delete, successor)
            successor.left = node_to_delete.left
            successor.left.p = successor

    def inorder_tree_walk(self, node, result):
        if node is not None:
            self.inorder_tree_walk(node.left, result)
            result.append(f"{{{node.key}, {node.value}}}")
            self.inorder_tree_walk(node.right, result)

    def __str__(self):
        result = []
        self.inorder_tree_walk(self.root, result)
        return "[" + ", ".join(result) + "]"
