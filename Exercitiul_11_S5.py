# 11. Definiti o funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea si împărțirea a două numere.

print('Rezolvare exercitiul 11 din tema sesiunii 5............................')


def add(a, b):
    result = a + b
    print(f'Suma numerelor este: {result}')
a = int(input("Introduceti un numar intreg  \n " ))
b = int(input("Introduceti un numar intreg  \n " ))
add(a=a, b=b)

def substract(a, b):
    substract = a - b
    print(f'Scaderea numerelor este: {substract}')
substract(a=a, b=b)

def multiply(a, b):
    multiply = a * b
    print(f'Inmultirea numerelor este: {multiply}')
multiply(a=a, b=b)

def divide(a, b):
    divide = a / b
    print(f'Impartirea numerelor este: {divide}')
divide(a=a, b=b)





