import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import numpy
import HashTable
import LinkedList
import ABR

if __name__ == "__main__":
    test_number = int(input("Inserisci il numero di test che si vogliono effettuare: "))
    search_success = int(input('Scegli se la ricerca debba avere successo oppure no(inserisci il numero): \n1. con '
                               'successo \n2. senza successo\n'))
    array_size = int(input("Inserisci la dimensione dell'array di numeri casuali: "))
    # print(my_list)

    t = 0

    A = HashTable.HashTable(int(input("Inserisci la dimensione della tabella hash: ")))
    nested_array_insert_hash = []
    nested_array_search_hash = []

    B = LinkedList.LinkedList()
    nested_array_insert_list = []
    nested_array_search_list = []

    tree = ABR.BinarySearchTree()
    nested_array_insert_abr = []
    nested_array_search_abr = []

    while t < test_number:

        my_list = [random.randint(0, 5000) for _ in range(array_size)]
        if search_success == 1:
            searched_value = random.choice(my_list)
        else:
            searched_value = 9999

        # TABELLA HASH #

        n = 0
        time_array_insert_hash = [0.0] * A.size
        start = timer()
        for value_hash in my_list:
            try:
                A.insert(value_hash)
                end = timer()
                time_array_insert_hash[n] = round(time_array_insert_hash[n - 1] + ((end - start) * 1000), 4)
                n = n + 1
            except IndexError:  # serve nel caso la tabella avesse dimensione inferiore all'array di elementi da inserire
                break
        # print(A.table)
        sub_array_insert_hash = []
        for i in range(A.size):
            sub_array_insert_hash.append(time_array_insert_hash[i])
        nested_array_insert_hash.append(sub_array_insert_hash)

        time_search_hash = A.search(searched_value)[1]
        A.delete(searched_value)
        # print(A.table)
        sub_array_search_hash = []
        for i in range(A.size):
            sub_array_search_hash.append(time_search_hash[i])
        nested_array_search_hash.append(sub_array_search_hash)

        last_non_zero_value = 0.0
        # Trova l'ultimo valore non zero nell'array
        for time_value in time_search_hash:
            if time_value != 0.0:
                last_non_zero_value = time_value

        # Assegna last_non_zero_value agli zeri successivi
        for i in range(len(time_search_hash)):
            if time_search_hash[i] == 0.0:
                time_search_hash[i] = last_non_zero_value

        # LISTA COLLEGATA #

        n = 0
        time_array_insert_list = [0.0] * array_size
        start = timer()
        for value_list in my_list:
            try:
                B.insert(value_list)
                end = timer()
                time_array_insert_list[n] = round(time_array_insert_list[n - 1] + ((end - start) * 1000), 4)
                n = n + 1
            except IndexError:
                break

        # print(time_array_insert_list)
        # print(B)
        # print(B.length)

        sub_array_insert_list = []
        for i in range(A.size):
            sub_array_insert_list.append(time_array_insert_list[i])
        nested_array_insert_list.append(sub_array_insert_list)

        b = B.search(searched_value)
        B.delete(searched_value)
        # print(b)
        # print(B)

        time_search_list = b[1]
        # non calcolo il tempo di delete poiché esegue una ricerca e poi aggiorna in tempo O(1) gli attributi dei nodi per
        # cancellarlo
        sub_array_search_list = []
        for i in range(A.size):
            sub_array_search_list.append(time_search_list[i])
        nested_array_search_list.append(sub_array_search_list)

        last_non_zero_value = 0.0
        # Trova l'ultimo valore non zero nell'array
        for time_value in time_search_list:
            if time_value != 0.0:
                last_non_zero_value = time_value

        # Assegna last_non_zero_value agli zeri successivi
        for i in range(len(time_search_list)):
            if time_search_list[i] == 0.0:
                time_search_list[i] = last_non_zero_value

        # ABR #

        n = 0
        time_array_insert_abr = [0.0] * array_size
        start = timer()
        for i, value in enumerate(my_list):
            tree.insert(i, value)
            end = timer()
            time_array_insert_abr[n] = round(time_array_insert_abr[n - 1] + ((end - start) * 1000), 4)
            n = n + 1

        sub_array_insert_abr = []
        for i in range(A.size):
            sub_array_insert_abr.append(time_array_insert_abr[i])
        nested_array_insert_abr.append(sub_array_insert_abr)

        c = tree.search(searched_value)
        tree.delete(searched_value)

        node, time_search_abr = c  # non calcolo il tempo di delete poiché esegue una ricerca

        sub_array_search_abr = []
        for i in range(A.size):
            sub_array_search_abr.append(time_search_abr[i])
        nested_array_search_abr.append(sub_array_search_abr)

        last_non_zero_value = 0.0
        # Trova l'ultimo valore non zero nell'array
        for time_value in time_search_abr:
            if time_value != 0.0:
                last_non_zero_value = time_value

        # Assegna last_non_zero_value agli zeri successivi
        for i in range(len(time_search_abr)):
            if time_search_abr[i] == 0.0:
                time_search_abr[i] = last_non_zero_value

        t += 1

    # HASH TABLE #

    mean_array_insert_hash = []
    for i in range(A.size):
        temp_array = []
        for sub_array in nested_array_insert_hash:
            temp_array.append(sub_array[i])
        mean_array_insert_hash.append(numpy.mean(temp_array))

    mean_array_search_hash = []
    for i in range(A.size):
        temp_array = []
        for sub_array in nested_array_search_hash:
            temp_array.append(sub_array[i])
        mean_array_search_hash.append(numpy.mean(temp_array))

    number_of_elements_arr = [0.0] * A.size
    x = 0
    while x < A.size:
        number_of_elements_arr[x] = number_of_elements_arr[x - 1] + 1
        x = x + 1
    plt.plot(number_of_elements_arr, mean_array_insert_hash, label='Insert')
    plt.plot(number_of_elements_arr, mean_array_search_hash,
             label='Search')  # il tempo della cancellazione è uguale a quello della ricerca
    plt.xlabel('Dimensione della tabella')
    plt.ylabel('Tempo di esecuzione (millisecondi)')
    plt.title('Tempi di esecuzione tabella hash')
    plt.legend()
    # plt.savefig(
    #     "D:/Università/Secondo anno/Algoritmi e Strutture Dati/Elaborato Laboratorio Maggio-Giugno/Grafici Esercizio "
    #     "1/THIS")
    plt.show()  # sarebbe meglio separare i due grafici di insert e search quando la ricerca va a buon fine

    # LISTA CONCATENATA #

    mean_array_insert_list = []
    for i in range(A.size):
        temp_array = []
        for sub_array in nested_array_insert_list:
            temp_array.append(sub_array[i])
        mean_array_insert_list.append(numpy.mean(temp_array))

    mean_array_search_list = []
    for i in range(A.size):
        temp_array = []
        for sub_array in nested_array_search_list:
            temp_array.append(sub_array[i])
        mean_array_search_list.append(numpy.mean(temp_array))

    # number_of_elements_arr = [0.0] * array_size
    # x = 0
    # while x < array_size:
    #     number_of_elements_arr[x] = number_of_elements_arr[x - 1] + 1
    #     x = x + 1
    plt.plot(number_of_elements_arr, mean_array_insert_list, label='Insert')
    plt.plot(number_of_elements_arr, mean_array_search_list,
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

    mean_array_insert_abr = []
    for i in range(A.size):
        temp_array = []
        for sub_array in nested_array_insert_abr:
            temp_array.append(sub_array[i])
        mean_array_insert_abr.append(numpy.mean(temp_array))

    mean_array_search_abr = []
    for i in range(A.size):
        temp_array = []
        for sub_array in nested_array_search_abr:
            temp_array.append(sub_array[i])
        mean_array_search_abr.append(numpy.mean(temp_array))

    # print(time_search_abr)
    # height = tree.height()
    # print(height)
    # number_of_elements_arr = [0.0] * array_size
    # x = 0
    # while x < array_size:
    #     number_of_elements_arr[x] = number_of_elements_arr[x - 1] + 1
    #     x = x + 1
    plt.plot(number_of_elements_arr, mean_array_insert_abr, label='Insert')
    plt.plot(number_of_elements_arr, mean_array_search_abr, label='Search')
    plt.xlabel('Dimensione dell\'albero')
    plt.ylabel('Tempo di esecuzione (millisecondi)')
    plt.title('Tempi di esecuzione ABR')
    plt.legend()
    # plt.savefig(
    #     "D:/Università/Secondo anno/Algoritmi e Strutture Dati/Elaborato Laboratorio Maggio-Giugno/Grafici Esercizio "
    #     "1/ABRIS")
    plt.show()  # sarebbe meglio separare i due grafici di insert e search quando la ricerca va a buon fine

    # CONFRONTO DEI METODI INSERT #

    plt.plot(number_of_elements_arr, mean_array_insert_hash, label="Insert HashTable")
    plt.plot(number_of_elements_arr, mean_array_insert_list, label="Insert LinkedList")
    plt.plot(number_of_elements_arr, mean_array_insert_abr, label="Insert ABR")
    plt.xlabel('Dimensione dell\'array da inserire (o della tabella per hash)')
    plt.ylabel('Tempo di esecuzione (millisecondi)')
    plt.title('Confronto tempi di esecuzione di insert')
    plt.legend()
    # plt.savefig(
    #     "D:/Università/Secondo anno/Algoritmi e Strutture Dati/Elaborato Laboratorio Maggio-Giugno/Grafici Esercizio "
    #     "1/ConfrIns")
    plt.show()

    # CONFRONTO DEI METODI SEARCH #
    plt.plot(number_of_elements_arr, mean_array_search_hash, label="Search HashTable")
    plt.plot(number_of_elements_arr, mean_array_search_list, label="Search LinkedList")
    plt.plot(number_of_elements_arr, mean_array_search_abr, label="Search ABR")
    plt.xlabel('Dimensione dell\'array da inserire (o della tabella per hash)')
    plt.ylabel('Tempo di esecuzione (millisecondi)')
    plt.title('Confronto tempi di esecuzione di search')
    plt.legend()
    # plt.savefig(
    #     "D:/Università/Secondo anno/Algoritmi e Strutture Dati/Elaborato Laboratorio Maggio-Giugno/Grafici Esercizio "
    #     "1/ConfrSearch")
    plt.show()
