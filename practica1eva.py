menu = True

while menu == True:
    print(f"~~~ CÁLCULO MATEMÁTICO ~~~\n")
    print(f"Selecciona una de las siguientes opciones...\n")
    print(f"1. Cálculo del perímetro de una circunferencia de radio r.")
    print(f"2. Cálculo del área de un círculo de radio r.")
    print(f"3. Cálculo del volumen de una esfera de radio r.")
    print(f"4. Salir del programa.\n")
    print(f"~~~~~ /\+/\-/\*/\^/\ ~~~~~\n")
    opcion = int(input("Inserta número: "))

    if opcion == 1:
        print(f"Has seleccionado la opción número 1.\n")
    else:
        input("\nLa opción seleccionada no existe. Por favor, vuelve a intentarlo. (Pulsa ENTER para reiniciar)")
        menu = False 