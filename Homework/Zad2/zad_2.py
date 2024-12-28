# 2. Zadanie: Usuwanie Duplikatów z Listy bez Użycia set()
# Usuń duplikaty z listy, ale bez użycia konwersji do zbioru (set()).

lista_z_duplikatami = [1, 2, 3, 2, 4, 5, 3, 6, 1]
nowa_lista = []
for i in lista_z_duplikatami:
    if i not in nowa_lista:
        nowa_lista.append(i)

print(nowa_lista)
