import random
import time
import matplotlib.pyplot as plt
import HashTable
import LinkedList
import ABR

if __name__ == "__main__":
    array_size = int(input("Inserisci la dimensione dell'array di numeri casuali: "))
    my_list = [random.randint(0, 5000) for _ in range(array_size)]
    print(my_list)

    # Tabella Hash #

    A = HashTable.HashTable(int(input("Inserisci la dimensione della tabella hash: ")))
    n = 0
    time_array_insert_hash = [0.0] * A.size
    start_hash = time.perf_counter()
    for value_hash in my_list:
        try:
            A.insert(value_hash)
            end_hash = time.perf_counter()
            time_array_insert_hash[n] = round(time_array_insert_hash[n - 1] + ((end_hash - start_hash) * 1000), 4)
            n = n + 1
        except IndexError:  # serve nel caso la tabella avesse dimensione inferiore all'array di elementi da inserire
            break
    print(A.table)

    time_search_hash = A.search(int(input("Inserisci il valore da ricercare nella tabella: ")))[1]
    A.delete(int(input("Inserisci il valore da cancellare dalla tabella: ")))
    print(A.table)

    last_non_zero_value = 0.0
    # Trova l'ultimo valore non zero nell'array
    for time_value in time_search_hash:
        if time_value != 0.0:
            last_non_zero_value = time_value

    # Assegna last_non_zero_value agli zeri successivi
    for i in range(len(time_search_hash)):
        if time_search_hash[i] == 0.0:
            time_search_hash[i] = last_non_zero_value

    number_of_elements_arr = [0.0] * A.size
    x = 0
    while x < A.size:
        number_of_elements_arr[x] = number_of_elements_arr[x - 1] + 1
        x = x + 1

    plt.plot(number_of_elements_arr, time_array_insert_hash, label='Insert')
    plt.plot(number_of_elements_arr, time_search_hash,
             label='Search')  # il tempo della cancellazione è uguale a quello della ricerca
    plt.xlabel('Dimensione della tabella')
    plt.ylabel('Tempo di esecuzione (millisecondi)')
    plt.title('Tempi di esecuzione tabella hash')
    plt.legend()
    # plt.savefig(
    #     "D:/Università/Secondo anno/Algoritmi e Strutture Dati/Elaborato Laboratorio Maggio-Giugno/Grafici Esercizio "
    #     "1/THIS")
    plt.show()  # sarebbe meglio separare i due grafici di insert e search quando la ricerca va a buon fine

    # Lista Collegata #

    B = LinkedList.LinkedList()

    n = 0
    time_array_insert_list = [0.0] * array_size
    start = time.perf_counter()
    for value_list in my_list:
        try:
            B.insert(value_list)
            end = time.perf_counter()
            time_array_insert_list[n] = round(time_array_insert_list[n - 1] + ((end - start) * 1000), 4)
            n = n + 1
        except IndexError:
            break

    print(time_array_insert_list)
    print(B)
    print(B.length)

    b = B.search(int(input("Inserisci il valore da cercare nella lista concatenata: ")))
    B.delete(int(input("Inserisci il valore da cancellare dalla lista concatenata: ")))
    print(b)
    print(B)

    time_search_list = b[1]
    # non calcolo il tempo di delete poiché esegue una ricerca e poi aggiorna in tempo O(1) gli attributi dei nodi per
    # cancellarlo

    last_non_zero_value = 0.0
    # Trova l'ultimo valore non zero nell'array
    for time_value in time_search_list:
        if time_value != 0.0:
            last_non_zero_value = time_value

    # Assegna last_non_zero_value agli zeri successivi
    for i in range(len(time_search_list)):
        if time_search_list[i] == 0.0:
            time_search_list[i] = last_non_zero_value

    # number_of_elements_arr = [0.0] * array_size
    # x = 0
    # while x < array_size:
    #     number_of_elements_arr[x] = number_of_elements_arr[x - 1] + 1
    #     x = x + 1
    plt.plot(number_of_elements_arr, time_array_insert_list, label='Insert')
    plt.plot(number_of_elements_arr, time_search_list,
             label='Search')  # il tempo della cancellazione è uguale a quello della ricerca (O(n))
    plt.xlabel('Dimensione della lista')
    plt.ylabel('Tempo di esecuzione (millisecondi)')
    plt.title('Tempi di esecuzione lista concatenata')
    plt.legend()
    # plt.savefig(
    #     "D:/Università/Secondo anno/Algoritmi e Strutture Dati/Elaborato Laboratorio Maggio-Giugno/Grafici Esercizio "
    #     "1/LCIS")
    plt.show()  # sarebbe meglio separare i due grafici di insert e search quando la ricerca va a buon fine

    # ABR #

    tree = ABR.BinarySearchTree()

    print(tree)

    n = 0
    time_array_insert_abr = [0.0] * array_size
    start = time.perf_counter()
    for i, value in enumerate(my_list):
        tree.insert(i, value)
        end = time.perf_counter()
        time_array_insert_abr[n] = round(time_array_insert_abr[n - 1] + ((end - start) * 1000), 4)
        n = n + 1

    c = tree.search(int(input("Inserisci il valore da cercare nell'albero: ")))
    tree.delete(int(input("Inserisci il valore da cancellare dall'albero: ")))

    node, time_search_abr = c  # non calcolo il tempo di delete poiché esegue una ricerca

    last_non_zero_value = 0.0
    # Trova l'ultimo valore non zero nell'array
    for time_value in time_search_abr:
        if time_value != 0.0:
            last_non_zero_value = time_value

    # Assegna last_non_zero_value agli zeri successivi
    for i in range(len(time_search_abr)):
        if time_search_abr[i] == 0.0:
            time_search_abr[i] = last_non_zero_value

    print(time_search_abr)
    height = tree.height()
    print(height)
    # number_of_elements_arr = [0.0] * array_size
    # x = 0
    # while x < array_size:
    #     number_of_elements_arr[x] = number_of_elements_arr[x - 1] + 1
    #     x = x + 1
    plt.plot(number_of_elements_arr, time_array_insert_abr, label='Insert')
    plt.plot(number_of_elements_arr, time_search_abr, label='Search')
    plt.xlabel('Dimensione dell\'albero')
    plt.ylabel('Tempo di esecuzione (millisecondi)')
    plt.title('Tempi di esecuzione ABR')
    plt.legend()
    # plt.savefig(
    #     "D:/Università/Secondo anno/Algoritmi e Strutture Dati/Elaborato Laboratorio Maggio-Giugno/Grafici Esercizio "
    #     "1/ABRIS")
    plt.show()  # sarebbe meglio separare i due grafici di insert e search quando la ricerca va a buon fine

    # Confronto dei metodi insert #
    plt.plot(number_of_elements_arr, time_array_insert_hash, label="Insert HashTable")
    plt.plot(number_of_elements_arr, time_array_insert_list, label="Insert LinkedList")
    plt.plot(number_of_elements_arr, time_array_insert_abr, label="Insert ABR")
    plt.xlabel('Dimensione dell\'array da inserire (o della tabella per hash)')
    plt.ylabel('Tempo di esecuzione (millisecondi)')
    plt.title('Confronto tempi di esecuzione di insert')
    plt.legend()
    # plt.savefig(
    #     "D:/Università/Secondo anno/Algoritmi e Strutture Dati/Elaborato Laboratorio Maggio-Giugno/Grafici Esercizio "
    #     "1/ConfrIns")
    plt.show()

    # Confronto dei metodi search #
    plt.plot(number_of_elements_arr, time_search_hash, label="Search HashTable")
    plt.plot(number_of_elements_arr, time_search_list, label="Search LinkedList")
    plt.plot(number_of_elements_arr, time_search_abr, label="Search ABR")
    plt.xlabel('Dimensione dell\'array da inserire (o della tabella per hash)')
    plt.ylabel('Tempo di esecuzione (millisecondi)')
    plt.title('Confronto tempi di esecuzione di search')
    plt.legend()
    # plt.savefig(
    #     "D:/Università/Secondo anno/Algoritmi e Strutture Dati/Elaborato Laboratorio Maggio-Giugno/Grafici Esercizio "
    #     "1/ConfrSearch")
    plt.show()
