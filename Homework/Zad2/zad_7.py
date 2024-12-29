# 7. Zadanie: Wypakowywanie Krotek w Pętli
# Mając listę krotek, wypakuj każdą krotkę w pętli i wykonaj operację na jej elementach.
krotki = [(2, 3), (4, 5), (6, 7), (8, 9)]

for i, j in krotki:
    suma = i + j
    odejmowanie = i - j

    print(f"Krotka {i} i {j}. Ich suma to {suma} a ich wnik odejmowania to {odejmowanie}")
