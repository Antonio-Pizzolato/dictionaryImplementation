import Dict


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = Dict.Dictionary(size)
        for i in range(size):
            self.table.put(i, None)

    def hash_function(self, value):
        return value - (value // self.size) * self.size

    def insert(self, value):
        key = self.hash_function(value)
        if self.table.get(key) is None or self.table.get(key) == "Deleted":
            self.table.put(key, value)
        else:
            i = (key + 1) - ((key + 1) // self.size) * self.size
            while i != key:
                if self.table.get(i) is None or self.table.get(key) == "Deleted":
                    self.table.put(i, value)
                    return
                i = (i + 1) - ((i + 1) // self.size) * self.size
            print("Errore: Overflow della tabella hash")

    def search(self, value):
        key = self.hash_function(value)
        if self.table.get(key) == value:
            return key
        elif self.table.get(key) is None:
            return print("Errore: Valore non trovato")
        else:
            i = (key + 1) - ((key + 1) // self.size) * self.size
            while i != key or self.table.get(key) is None:
                if self.table.get(i) == value:
                    return i
                i = (i + 1) - ((i + 1) // self.size) * self.size
            return print("Errore: Valore non trovato")

    def delete(self, value):
        key = self.search(value)
        if key is None:
            return  # print("Errore: Valore non trovato")
        else:
            self.table.put(key, "Deleted")
            return print(self.table.get(key))
