class Node:
    def __init__(self, value):
        self.previous = None
        self.value = value
        self.next = None

    def __str__(self):
        return f"{{previous: {self.previous.value if self.previous else None}, value: {self.value}, next: {self.next.value if self.next else None}}}"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def search(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return current_node
            current_node = current_node.next
        return None

    def delete(self, value):
        node_to_delete = self.search(value)
        if node_to_delete:
            if node_to_delete.previous:
                node_to_delete.previous.next = node_to_delete.next
            else:
                self.head = node_to_delete.next
                if self.head:
                    self.head.previous = None
            if node_to_delete.next:
                node_to_delete.next.previous = node_to_delete.previous
            else:
                self.tail = node_to_delete.previous
                if self.tail:
                    self.tail.next = None
            del node_to_delete
            return True
        return False

    def __str__(self):
        current_node = self.head
        nodes = []
        while current_node:
            nodes.append(str(current_node))
            current_node = current_node.next
        return "[" + ", ".join(nodes) + "]"
