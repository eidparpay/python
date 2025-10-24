# Ejercicio 3
a = float(input("Ingrese el extremo A del intervalo (A, B]: "))
b = float(input("Ingrese el extremo B del intervalo (A, B]: "))
x = float(input("Ingrese el valor de X: "))

if a < x <= b:
    print(f"{x} pertenece al intervalo ({a}, {b}]")
else:
    print(f"{x} NO pertenece al intervalo ({a}, {b}]")
