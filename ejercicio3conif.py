# Ejercicio 4
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
num4 = int(input("Ingrese el cuarto número: "))

if num1 > num2:
    if num1 > num3:
        if num1 > num4:
            print("El mayor número es el ", num1)
        else:
            print("El mayor número es el ", num4)
    elif num3 > num4:
        if num3 > num2:
            print("El amyor número es el ", num3)
        else:
            print("El mayor número es el ", num2)
else:
    if num2 > num3:
        if num2 > num4:
            print("El mayor número es el ", num2)
        else:
            print("El mayor número es el ", num4)
    elif num3 > num4:
        if num3 > num1:
            print("El mayor número es el ", num3)
        else:
            print("El mayor número es el ", num1)

# Determinar el mayor
# mayor = max(num1, num2, num3, num4)

# print(f"El número mayor es: {mayor}")
