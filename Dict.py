class Dictionary:
    def __init__(self):
        self.keys = []
        self.values = []

    def __setitem__(self, key, value):
        index = self.keys.index(
            key) if key in self.keys else None  # il metodo index() restituisce l'indice corrispondente alla posizione dell'elemento key (se io inserisco d[1] = value lui cercherà alla posizione 1 dell'array, se 1 è presente nell'array allora assegna il valore 1 a index, altrimenti assegna None)
        if index is not None:
            self.values[index] = value
        else:
            self.keys.append(key)
            self.values.append(value)

    def __getitem__(self, key):
        index = self.keys.index(key)
        return self.values[index]

    def __delitem__(self, key):
        index = self.keys.index(key)
        del self.keys[index]
        del self.values[index]

    def __str__(self):
        pairs = [f"{key}: {value}" for key, value in zip(self.keys, self.values)]
        return "{" + ", ".join(pairs) + "}"


d = Dictionary()
print(d)
