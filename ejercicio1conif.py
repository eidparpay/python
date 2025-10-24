edad1 = int(input("¿Cuál es la edad de Juan?"))
edad2 = int(input("¿Cúal es la edad de Pedro?"))

if edad1 > edad2:
    edadDif = edad1 - edad2
    print("Juan es mayor que Pedro por ", edadDif, " años.")
elif edad2 > edad1:
    edadDif = edad2 - edad1
    print("Pedro es mayor que Juan por ", edadDif, " años.")
elif edad1 == edad2:
    print("Los dos tienen ", edad1, " años.")