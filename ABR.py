import time


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
        self.node_count = 0

    def insert(self, key, value):  # tempo O(nlgn)
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
        self.node_count += 1

    def search(self, value):  # versione iterativa più veloce della ricorsiva
        current_node = self.root
        start_s = time.perf_counter()
        time_array_search = [0.0] * self.node_count
        n_s = 0
        while current_node is not None:
            if value == current_node.value:
                end_s = time.perf_counter()
                time_array_search[n_s] = round(time_array_search[n_s - 1] + ((end_s - start_s) * 1000), 4)
                print("Key:", current_node.key, "Value:", current_node.value)
                return current_node, time_array_search
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
            end_s = time.perf_counter()
            time_array_search[n_s] = round(time_array_search[n_s - 1] + ((end_s - start_s) * 1000), 4)
            n_s = n_s + 1
        print("Errore: Valore non trovato")
        return None, time_array_search

    def minimum(self, node):
        while node.left is not None:
            node = node.left
        return node

    def successor(self, node):
        if node.right is not None:
            return self.minimum(node.right)
        parent = node.parent
        while parent is not None and node == parent.right:
            node = parent
            parent = parent.parent
        return parent

    def transplant(self, node1, node2):
        if node1.parent is None:
            self.root = node2
        elif node1 == node1.parent.left:
            node1.parent.left = node2
        else:
            node1.right = node2
        if node2 is not None:
            node2.parent = node1.parent

    def delete(self, value):  # tempo di delete è uguale a quello di search (O(h))
        node = self.search(value)
        node_to_delete, time_s = node

        if node_to_delete is None:
            return

        if node_to_delete.left is None:
            self.transplant(node_to_delete, node_to_delete.right)
        elif node_to_delete.right is None:
            self.transplant(node_to_delete, node_to_delete.left)
        else:
            successor = self.minimum(node_to_delete.right)
            if successor.parent != node_to_delete:
                self.transplant(successor, successor.right)
                successor.right = node_to_delete.right
                successor.right.parent = successor
            self.transplant(node_to_delete, successor)
            successor.left = node_to_delete.left
            successor.left.parent = successor

    def inorder_tree_walk(self, node, result):
        if node is not None:
            self.inorder_tree_walk(node.left, result)
            result.append(f"{{{node.key}, {node.value}}}")
            self.inorder_tree_walk(node.right, result)

    def height(self):
        return self.calculate_height(self.root)

    def calculate_height(self, node):
        if node is None:
            return -1
        left_height = self.calculate_height(node.left)
        right_height = self.calculate_height(node.right)
        return max(left_height, right_height) + 1

    def get_node_count(self):
        return self.node_count

    def __str__(self):
        result = []
        self.inorder_tree_walk(self.root, result)
        return "[" + ", ".join(result) + "]"
