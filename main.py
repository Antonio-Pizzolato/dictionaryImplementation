import random
import time
import matplotlib.pyplot as plt
import HashTable
import LinkedList
import ABR

array_size = int(input("Inserisci la dimensione dell'array di numeri casuali: "))
my_list = [random.randint(0, 5000) for _ in range(array_size)]
print(my_list)

# Tabella Hash #

A = HashTable.HashTable(int(input("Inserisci la dimensione della tabella hash: ")))
n = 0
time_array_insert = [0.0] * A.size
start = time.perf_counter()
for value in my_list:
    try:
        A.insert(value)
        end = time.perf_counter()
        time_array_insert[n] = round(time_array_insert[n - 1] + ((end - start) * 1000), 4)
        n = n + 1
    except IndexError:
        break
print(A.table)

time_search = A.search(int(input("Inserisci il valore da ricercare nella tabella: ")))[1]
A.delete(int(input("Inserisci il valore da cancellare dalla tabella: ")))
print(A.table)

number_of_elements_arr = [0.0] * A.size
x = 0
while x < A.size:
    number_of_elements_arr[x] = number_of_elements_arr[x - 1] + 1
    x = x + 1

plt.plot(number_of_elements_arr, time_array_insert, label='Insert')
plt.plot(number_of_elements_arr, time_search, label='Search')  # il tempo della cancellazione è uguale a quello della ricerca
plt.xlabel('Dimensione della tabella')
plt.ylabel('Tempo di esecuzione (millisecondi)')
plt.title('Tempi di esecuzione dei metodi')
plt.legend()
plt.show() #sarebbe meglio separare i due grafici di insert e search quando la ricerca va a buon fine

# # Lista Collegata #
#
# B = LinkedList.LinkedList()
# for value in my_list:
#     B.insert(value)
#
# print(B)
#
# B.delete(int(input("Inserisci il valore da cancellare dalla tabella: ")))
# b = B.search(int(input("Inserisci il valore da cercare nella tabella: ")))
# print(b)
# print(B)


# # ABR #
#
# tree = ABR.BinarySearchTree()
# for i, value in enumerate(my_list):
#     tree.insert(i, value)
#
# print(tree)
