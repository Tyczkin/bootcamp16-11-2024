# 1. Stwórz Listę
# Stwórz listę zawierającą pięć różnych owoców.
owoce = ['banan', 'cytryna', 'kiwi', 'truskawka', 'jagoda']
print(owoce)

# 2. Znajdź Drugi Element Listy
# Mając listę, znajdź drugi element listy.
print("Oto drugi element listy:", owoce[1])

# 3. Zmień Element w Liście
# Zmień trzeci element listy na "malina".
owoce[2] = 'malina'
print("Nowa lista za zmienionym trzecim elementem:", owoce)

# 4. Stwórz Krotkę
# Stwórz krotkę zawierającą trzy różne kolory.
kolory = 'czerwony', 'niebieski', 'zielony'
print(kolory)

# 5. Wybierz Ostatni Element Krotki
# Mając krotkę, wybierz jej ostatni element.
print("Ostatni element krotki kolorow:", kolory[-1])

# 8. Stwórz String Zawierający Twoje Imię i Nazwisko
# Stwórz string "Jan Kowalski".
nazwa = 'Sebastian Tyka'

# 9. Podziel String na Imię i Nazwisko
# Podziel powyższy string na dwa osobne stringi: imię i nazwisko.
lista = nazwa.split()
imie = lista[0]
nazwisko = lista[1]
print(imie, nazwisko)

# 10. Użyj F-stringa do Połączenia Tekstu
# Stwórz string "Mam na imię Jan i mam 25 lat" używając f-stringa.
print(f'Mam na imie {imie} i mam 25 lat')

# 1. Zadanie: Znajdź Długość Listy
# Mając listę [1, 2, 3, 4, 5], znajdź jej długość.
lista_1 = [1, 2, 3, 4, 5]
print("Dlugosc listy", lista_1, " wynosi:", (lista_1))

# 2. Zadanie: Połącz Dwie Listy
# Mając dwie listy, na przykład [1, 2, 3] i [4, 5, 6], połącz je w jedną.
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2
print("Polaczone dwie listy 1,2,3 i 4,5,6:", l3)

# 3. Zadanie: Dodaj Element na Końcu Listy
# Dodaj nowy element na końcu listy [1, 2, 3], na przykład 4.
lista_2 = [1, 2, 3]
lista_2.append(4)
print("Dodany nowy element na koncu listy:", lista_2)

# 4. Zadanie: Wybierz Element z Krotki
# Mając krotkę (1, 2, 3, 4, 5), wybierz trzeci element.
krotka = (1, 2, 3, 4, 5)
print("Trzeci element krotki 1,2,3,4,5 to:", krotka[2])

# 5. Zadanie: Odwróć Listę
# Odwróć kolejność elementów w liście [1, 2, 3, 4, 5].
lista_3 = [1, 2, 3, 4, 5]
print("Odwrocona lista [1,2,3,4,5] to :", lista_3[::-1])
# 6. Zadanie: Znajdź Maksymalny Element w Liście
# Znajdź największy element w liście [1, 2, 3, 4, 5].
print("Wartosc max w liscie:", max(lista_3))

# 7. Zadanie: Formatowanie Stringa
# Stwórz string "Python", a następnie dodaj do niego string " jest super!", tworząc pełne zdanie.
zmienna = 'Python'
print("Formatowanie stringa:", zmienna + ' jest super!')

# 8. Zadanie: Zastąp Słowo w Stringu
# Mając string "Lubię Pythona", zastąp słowo "Pythona" słowem "programowanie".
zmienna1 = "Lubie Pythona"
print("Zastapienie slowa Python slowem programowanie:")
print("Przed:", zmienna1)
nowa_zmienna = zmienna1.replace('Pythona', 'programowanie')
print("Po:", nowa_zmienna)

# 9. Zadanie: Wyodrębnij Podstring
# Wyodrębnij słowo "Python" ze stringa "Lubię Pythona".
zmienna2 = "Lubie Pythona"
podstring = 'Python'
indeks = zmienna2.index((podstring))
print(indeks)
zmienna3 = zmienna2[indeks:len(zmienna2) - 1]
print(zmienna3)
# 10. Zadanie: Stwórz Listę Liczb Nieparzystych
# Stwórz listę zawierającą pierwsze pięć liczb nieparzystych.
lista_nieparzysta = [1,3,5,7,9]