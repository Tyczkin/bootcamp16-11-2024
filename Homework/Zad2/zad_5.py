#5. Zadanie: Implementacja Własnego Algorytmu Sortowania
#Zaimplementuj prosty algorytm sortowania (np. sortowanie bąbelkowe) i użyj go do posortowania listy.
from functools import reduce

lista_nieposortowana = [42, 7, 19, 3, 56, 1, 23, 8]
while True:
    zmiana = False
    for i in range(len(lista_nieposortowana)-1):

        if lista_nieposortowana[i] > lista_nieposortowana[i + 1]:
            temp = lista_nieposortowana[i]
            lista_nieposortowana[i] = lista_nieposortowana[i + 1]
            lista_nieposortowana[i + 1] = temp
            zmiana = True
    if not zmiana:
        break

print(lista_nieposortowana)

