# 3. Zadanie: Znajdowanie Wszystkich Par Liczb Sumujących się do Określonej Wartości
# Dla danej listy liczb i wartości docelowej, znajdź wszystkie pary liczb w liście, które sumują się do tej wartości.

lista_liczb = [2, 4, 3, 7, 5, 1, 9, 6]
wartosc_docelowa = 10
lista_par = []
for i in lista_liczb:
    for j in lista_liczb:
        if i + j == wartosc_docelowa:
            a = (i, j)
            lista_par.append(a)

print(lista_par)