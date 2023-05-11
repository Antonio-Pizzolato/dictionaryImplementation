import random
import HashTable

array_size = int(input("Inserisci la dimensione dell'array di numeri casuali: "))
my_list = [random.randint(0, 5000) for _ in range(array_size)]
print(my_list)

A = HashTable.HashTable(int(input("Inserisci la dimensione della tabella hash: ")))
for value in my_list:
    A.insert(value)

print(A.table)

A.delete(int(input("Inserisci il valore da cancellare dalla tabella: ")))
A.search(int(input("Inserisci il valore da ricercare nella tabella: ")))
print(A.table)
