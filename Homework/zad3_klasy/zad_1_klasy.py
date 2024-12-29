#zad1
#--------
# stworzenie ksiazki telefonicznej z wykorzystanie petli while True
# dodaj kontakt, usun kontakt, wyszukaj kontakt, wyswietl kontakty

class KsiazkaTelefoniczna:
    def __init__(self):
        self.slownik = {}

    def dodaj_kontakt(self,imie,naziwsko,telefon):
        if telefon not in self.slownik.keys():
            self.slownik[telefon] = [imie,naziwsko]
            print(f"Dodales {imie} {naziwsko} (tel.{telefon})")
        else:
            print(f"Telefon o numerze {telefon} juz istnieje w ksiazce telefonicznej")

    def wyswietl_kontakty(self):
        print("Kontakty:")
        for telefon, imie_i_naziwsko in self.slownik.items():
            print(f"{telefon} - {imie_i_naziwsko}")

    def wyszukaj(self,telefon):
        if telefon in self.slownik:
            imie,nazwisko = self.slownik[telefon]
            print(f"Znaleziono kontakt {imie} {nazwisko}. Prosze dzwonic pod numer telefonu:{telefon}")
        else:
            print("Kontakt nie istnieje.")

    def usun_kontakt(self,telefon):
        if telefon in self.slownik:
            self.slownik.pop(telefon)
            print(f"Kontakt {telefon} usuniety")
        else:
            print("Kontakt nie istnieje")


czlowiek = KsiazkaTelefoniczna()

while True:
    print("""
    Witaj w Ksiazce Telefonicznej. Wprowadz numer opercji ktora chcesz wykonac:
    1. Dodaj Kontakt
    2. Wyszukaj Kontakt
    3. Wyswietl kontakty
    4. Usun kontakt
    0. Wyjscie""")
    wybor = int(input("Wprowadz nr: >>"))

    if wybor == 1:
        imie = str(input("Wprowadz imie: >>")).capitalize()
        nazwisko = str(input("Wprowadz nazwisko: >>")).capitalize()
        tel = str(input("Wprowadz numer telefonu: >>"))
        czlowiek.dodaj_kontakt(imie,nazwisko,tel)

    elif wybor == 2:
        tel = str(input("Wprowadz numer telefonu: >>"))
        czlowiek.wyszukaj(tel)

    elif wybor == 3:
        czlowiek.wyswietl_kontakty()

    elif wybor == 4:
        tel = str(input("Wprowadz numer telefonu: >>"))
        czlowiek.usun_kontakt(tel)

    elif wybor == 0:
        print("Wyszedles z ksiazki telefonicznej.")
        break

    else:
        print("Nie wybrales poprawnie numeru!")