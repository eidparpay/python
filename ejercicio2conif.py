# Ejercicio 2
x = int(input("Ingrese el valor de X: "))
y = int(input("Ingrese el valor de Y: "))

# Verificar si X es múltiplo de Y
if y != 0:
    if x % y == 0:
        print(f"{x} es múltiplo de {y}")
    else:
        print(f"{x} no es múltiplo de {y}")
else:
    print("No se puede dividir por 0, Y no puede ser 0.")

# Verificar si X es par
if x % 2 == 0:
    print(f"{x} es par")
else:
    print(f"{x} es impar")
