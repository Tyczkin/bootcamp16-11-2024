# zbior = set

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]

zbior = set(lista)
print(zbior)

lista2 = list(zbior)
lista2.remove(33)
print(lista2)

# utworzenie pustego seta
zb2 = set()

print(type(zb2))

# dodawanie elementow do zbioru

zb2.add(2)
zb2.add(3)
zb2.add(5)
zb2.add(5)
zb2.add(3)

print(zb2)
print(zbior)

zbior.add(33)

# tworzenie zbioru z konkretnymi elementami
zbior2 = {667, 11, 44, 18, 52, 22, 667, 62, 999}
zbior3 = {11,44,22,5,6,7}

print(zbior2 & zbior3)

frozen = frozenset([1,2,3])

print(frozen)

zb3 = {1,2,3,4,5,6,7,8,9}
print(sum(zb3))
print(max(zb3))