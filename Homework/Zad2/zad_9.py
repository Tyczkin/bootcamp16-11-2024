#9. Zadanie: Przeszukiwanie Listy za Pomocą Wyrażeń Listowych (List Comprehensions)
#Stwórz listę kwadratów liczb parzystych z danej listy liczb przy użyciu wyrażeń listowych.

lista_liczb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_kwadratow = [i*i for i in lista_liczb if i % 2 == 0]
print(lista_kwadratow)