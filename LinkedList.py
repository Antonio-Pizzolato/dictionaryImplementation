import time


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
        self.length = 0

    def insert(self, value):  # tempo O(1)
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def ordered_insert(self, value):
        new_node = Node(value)

        # Se la lista è vuota
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return

        # Caso in cui il nuovo nodo deve essere inserito all'inizio della lista
        if value < self.head.value:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
            self.length += 1
            return

        current = self.head
        while current.next is not None and value > current.next.value:
            current = current.next

        # Caso in cui il nuovo nodo deve essere inserito nel mezzo della lista
        new_node.next = current.next
        if current.next is not None:
            current.next.previous = new_node
        current.next = new_node
        new_node.previous = current

        # Caso in cui il nuovo nodo deve essere inserito alla fine della lista
        if current == self.tail:
            self.tail = new_node

        self.length += 1

    def search(self, value):
        current_node = self.head
        start_s = time.perf_counter()
        time_array_search = [0.0] * self.length
        n_s = 0
        while current_node is not None:
            if current_node.value == value:
                end_s = time.perf_counter()
                time_array_search[n_s] = round(time_array_search[n_s - 1] + ((end_s - start_s) * 1000), 4)
                return current_node, time_array_search
            current_node = current_node.next
            end_s = time.perf_counter()
            time_array_search[n_s] = round(time_array_search[n_s - 1] + ((end_s - start_s) * 1000), 4)
            n_s = n_s + 1
        print("Errore: Valore non trovato")
        return None, time_array_search

    def delete(self, value):
        node_to_delete = self.search(value)
        node = node_to_delete[0]
        if node is Node:
            if node.previous:
                node.previous.next = node.next
            else:
                self.head = node.next
                if self.head:
                    self.head.previous = None
            if node.next:
                node.next.previous = node.previous
            else:
                self.tail = node.previous
                if self.tail:
                    self.tail.next = None
            del node
            self.length -= 1
            return True
        return False

    def __str__(self):
        current_node = self.head
        nodes = []
        while current_node:
            nodes.append(str(current_node))
            current_node = current_node.next
        return "[" + ", ".join(nodes) + "]"
