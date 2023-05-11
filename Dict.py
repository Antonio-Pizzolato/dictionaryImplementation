class Dictionary:
    def __init__(self, size):
        self.items = [] * size

    # aggiunge o aggiorna una coppia chiave-valore nella lista (mette value in key)
    def put(self, key, value):
        for item in self.items:
            if item[0] == key:
                item[1] = value
                return
        self.items.append([key, value])

    # restituisce il valore associato a una data chiave, sollevando un'eccezione KeyError se la chiave non esiste
    def get(self, key):
        for item in self.items:
            if item[0] == key:
                return item[1]
        raise KeyError(f"Key '{key}' not found")

    # rimuove la coppia chiave-valore associata a una data chiave, sollevando un'eccezione KeyError se la chiave non
    # esiste
    def remove(self, key):
        for i in range(len(self.items)):
            if self.items[i][0] == key:
                self.items.pop(i)
                return
        raise KeyError(f"Key '{key}' not found")

    # restituiscono rispettivamente una lista delle chiavi, una lista dei valori e una lista di tuple chiave-valore
    def keys(self):
        return [item[0] for item in self.items]

    def values(self):
        return [item[1] for item in self.items]

    def items(self):
        return self.items.copy()

    def __str__(self):
        return "[" + ", ".join([f"{{{k}: {v}}}" for k, v in self.items]) + "]"
