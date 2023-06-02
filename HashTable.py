import math
import time


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [{key: None} for key in range(size)]
        self.function = int(input('Choose what function to use (insert the number): \n1. linear hash \n2. quadratic hash \n3. double hash\n'))
        if self.function == 1:
            self.hash_function = self.linear_hash_function
        elif self.function == 2:
            self.hash_function = self.quadratic_hash
        elif self.function == 3:
            self.hash_function = self.double_hash
        self.count = 0

    def linear_hash_function(self, value, i):
        h1 = value - (value // self.size) * self.size
        return (h1 + i) - ((h1 + i) // self.size) * self.size

    def quadratic_hash(self, value, i):
        h1 = value - (value // self.size) * self.size
        return (h1 + (1 * i) + (10 * (i ** 2))) % self.size

    def double_hash(self, value, i):
        h1 = value - (value // self.size) * self.size
        h2 = self.next_prime(self.size - 2)
        return (h1 + i * h2) % self.size

    def next_prime(self, n):
        if n < 2:
            return 2
        prime = n + 1
        while not self.is_prime(prime):
            prime += 1
        return prime

    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def alternative_double_hash(self, value, i):
        h1 = value - (value // self.size) * self.size
        h2 = value % (self.size - 1)
        return math.floor((h1 + i * h2) % self.size)

    def insert(self, value):
        i = 0
        while i < self.size:
            key = self.hash_function(value, i)
            if self.table[key] == {key: None} or self.table[key] == {key: "Deleted"}:
                self.table[key] = {key: value}
                self.count += 1
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
            if self.table[key] == {key: value}:
                end_s = time.perf_counter()
                time_array_search[n_s] = round(time_array_search[n_s - 1] + ((end_s - start_s) * 1000), 4)
                return key, time_array_search
            i = i + 1
            if self.table[key] == {key: None} or self.table[key] == {key: "Deleted"} or i >= self.size:
                end_s = time.perf_counter()
                time_array_search[n_s] = round(time_array_search[n_s - 1] + ((end_s - start_s) * 1000), 4)
                print("Errore: Valore non trovato")
                return None, time_array_search
            end_s = time.perf_counter()
            time_array_search[n_s] = round(time_array_search[n_s - 1] + ((end_s - start_s) * 1000), 4)
            n_s = n_s + 1

    def delete(self, value):
        key = self.search(value)
        if key[0] is None:
            return print("Errore: Valore non trovato")
        else:
            self.table[key[0]] = {key[0]: "Deleted"}
            self.count -= 1
            return print(self.table[key[0]])

    def __str__(self):
        items = [f"{{{key}: {value[key]}}}" if value[key] is not None else f"{{{key}: None}}" for key, value in enumerate(self.table)]
        return "[" + ", ".join(items) + "]"
