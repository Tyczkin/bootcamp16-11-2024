# 6. Zadanie: Formatowanie Stringa z Wykorzystaniem Metody .format()
# Stwórz złożony string używając metody .format() oraz słownika.

slownik = {
    "name":"Sebastian",
    "age":100,
    "hobby":"malarstwo",
    "city":"Krakow"
}

zdanie = "Czesc, mam na imie {} i mam {} lat. Mieszkam w {} a moje hobby to {}!".format(slownik["name"],
                                                                                        slownik["age"],
                                                                                        slownik["city"],
                                                                                        slownik["hobby"])

print(zdanie)