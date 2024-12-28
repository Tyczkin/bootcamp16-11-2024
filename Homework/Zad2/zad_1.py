# 1. Zadanie: Wyodrębnienie Elementów z Listy List
# Mając listę list (na przykład [[1, 2], [3, 4], [5, 6]]), stwórz nową listę,
# zawierającą tylko drugie elementy każdej wewnętrznej listy.

lista = [[1, 2], [3, 4], [5, 6]]

nowa_lista = [i[1] for i in lista]

print(nowa_lista)