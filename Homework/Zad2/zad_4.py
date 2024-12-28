# 4. Zadanie: Sortowanie Listy Krotek
# Posortuj listę krotek po drugim elemencie każdej krotki (na przykład [(1, 3), (3, 2), (2, 1)]).

lista_krotek = [(1, 3), (3, 2), (2, 1)]
posortowana_lista = sorted(lista_krotek,key= lambda x: x[1])
print(posortowana_lista)