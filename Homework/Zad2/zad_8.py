#8. Zadanie: Utworzenie Generatora Liczb Fibonacciego
#Napisz generator, który wyprowadza kolejne liczby z ciągu Fibonacciego.

def fibonacci_generator():
    i = 0
    j = 1
    while True:
        yield i
        i, j = j, i + j

generuj = fibonacci_generator()
for _ in range(10):
    print(next(generuj))