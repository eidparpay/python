menu = True

while menu == True:
    print(f"~~~ CÁLCULO MATEMÁTICO ~~~\n")
    print(f"Selecciona una de las siguientes opciones...\n")
    print(f"1. Cálculo del perímetro de una circunferencia de radio r.")
    print(f"2. Cálculo del área de un círculo de radio r.")
    print(f"3. Cálculo del volumen de una esfera de radio r.")
    print(f"4. Salir del programa.\n")
    print(f"~~~~~ /\+/\-/\*/\^/\ ~~~~~\n")
    opcion = int(input("Inserta número de opción: "))

    if opcion == (1 or 2 or 3):
        unidad = str(input(f"\nEscribe las unidades con las que quieres trabajar (mm, cm, m, km): "))
        menu = False
    elif opcion == (4):
        print(f"\nCerrando programa...\n")
        menu = False
        exit
    else:
        input("\nLa opción seleccionada no existe. Por favor, vuelve a intentarlo. (Pulsa ENTER para reiniciar)\n\n")
        menu = False
        menu = True
if opcion == (1):
    print(f"\nHas seleccionado la opción número 1.\n")
    print(f"La fórmula que vamos a utilizar es P = 2πr.\n")
    radio = float(input(f"Introduce el radio de la circunferencia en {unidad}: "))
    resultado = round(2 * 3.1415 * radio, 2)
    print(f"\nEl perímetro de la circunferencia es de {resultado} {unidad}.")
    repetir = str(input(f"¿Quieres realizar otra operación? (S/N) "))
    menu = True
    if repetir == ("S"):
        menu = True
    else:
        exit