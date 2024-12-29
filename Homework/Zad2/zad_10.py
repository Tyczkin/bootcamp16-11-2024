#10. Zadanie: Stwórz Funkcję Formatującą Adresy Email
#Napisz funkcję, która przyjmuje listę imion i nazwisk, a zwraca sformatowane adresy email
#(np. Jan Kowalski -> jan.kowalski@example.com).

def email_format(imie,nazwisko,nazwa_domeny = '@example.com'):
    adres_email = f"{imie.lower()}.{nazwisko.lower()}{nazwa_domeny.lower()}"
    return adres_email

print(email_format('Tomek',"Nowak"))
