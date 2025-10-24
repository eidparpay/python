# Ejercicio 4
x = float(input("Ingrese el valor de X: "))
y = float(input("Ingrese el valor de Y: "))

if x > y:
    mayor = x
    menor = y
elif y > x:
    mayor = y
    menor = x
else:
    print("Ambos números son iguales.")
    exit()

porcentaje = (menor / mayor) * 100
print(f"El número mayor es {mayor}")
print(f"El menor representa el {porcentaje:.2f}% del mayor")
