import Dict
import time


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = Dict.Dictionary(size)
        for i in range(size):
            self.table.put(i, None)

    def hash_function(self, value, i):
        x = value - (value // self.size) * self.size
        return (x + i) - ((x + i) // self.size) * self.size

    def insert(self, value): # teoricamente l'enorme aumento del tempo di inserimento negli ultimi elementi è dovuto al clustering
        i = 0
        while i < self.size:
            key = self.hash_function(value, i)
            if self.table.get(key) is None or self.table.get(key) == "Deleted":
                self.table.put(key, value)
                return
            else:
                i = i + 1
        print("Errore: Overflow della tabella hash")
        return

    def search(self, value):
        i = 0
        start_s = time.perf_counter()
        time_array_search = [0.0] * self.size
        n_s = 0
        while i < self.size:
            key = self.hash_function(value, i)
            if self.table.get(key) == value:
                end_s = time.perf_counter()
                time_array_search[n_s] = round(time_array_search[n_s - 1] + ((end_s - start_s) * 1000), 4)
                return key, time_array_search
            i = i + 1
            if self.table.get(key) is None or self.table.get(key) == "Deleted" or i >= self.size:
                end_s = time.perf_counter()
                time_array_search[n_s] = round(time_array_search[n_s - 1] + ((end_s - start_s) * 1000), 4)
                print("Errore: Valore non trovato")
                return None, time_array_search
            end_s = time.perf_counter()
            time_array_search[n_s] = round(time_array_search[n_s - 1] + ((end_s - start_s) * 1000), 4)
            n_s = n_s + 1

    def delete(self, value):
        key = self.search(value)
        if key[0] is None:  # key non ritorna None perchè ho aggiunto un valore da ritornare a search
            return print("Errore: Valore non trovato")
        else:
            self.table.put(key[0], "Deleted")
            return print(self.table.get(key[0]))
