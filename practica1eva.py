menuPrincipal = True
menuUnidad = False
unidadPer = ['mm', 'cm', 'm', 'km']
mm = 0
cm = 1
m = 2
km = 3
valorUnidad = [mm, cm, m, km]
valorUnidadCon = [mm, cm, m, km]
conversion = float(1)

while menuPrincipal == True:
    print(f"\n\n\n\n\n~~~ CÁLCULO MATEMÁTICO ~~~\n")
    print(f"Selecciona una de las siguientes opciones...\n")
    print(f"1. Cálculo del perímetro de una circunferencia de radio r.")
    print(f"2. Cálculo del área de un círculo de radio r.")
    print(f"3. Cálculo del volumen de una esfera de radio r.")
    print(f"4. Salir del programa.\n")
    print(f"~~~~~ /\+/\-/\*/\^/\ ~~~~~\n")
    opcion = (int(input("Inserta número de opción: ")))
    if opcion == 1 or opcion == 2 or opcion == 3:
        menuUnidad = True
        while menuUnidad == True:
            unidadSel = (input(f"\nEscribe las unidades con las que quieres trabajar (mm, cm, m, km): "))
            if unidadSel not in unidadPer:
                input("\nLa unidad seleccionada no existe. Por favor, vuelve a intentarlo. (Pulsa ENTER para volver a introducir la unidad)")
            else:
                menuUnidad = False
                menuPrincipal = False
                menuUnidadCon = True
                while menuUnidadCon == True:
                    unidadSelCon = (input(f"\nEscribe las unidades a las que quieras convertir (mm, cm, m, km): "))
                    if unidadSel not in unidadPer:
                        input("\nLa unidad seleccionada no existe. Por favor, vuelve a intentarlo. (Pulsa ENTER para volver a introducir la unidad)")
                    else:
                        unidadSel[0] = mm
                        unidadSelCon[0] = mm
                        unidadSel[1] = cm
                        unidadSelCon[1] = cm
                        unidadSel[2] = m
                        unidadSelCon[2] = m
                        unidadSel[3] = km
                        unidadSelCon[3] = km
                        while valorUnidad != valorUnidadCon:
                            if valorUnidadCon > valorUnidad:
                                conversion = float(conversion / 10)
                                valorUnidad = valorUnidad[+1]
                            elif valorUnidadCon < valorUnidad:
                                conversion = float(conversion * 10)
                                valorUnidad = valorUnidad[-1]
                        menuUnidadCon = False      
            if opcion == (1):
                print(f"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(f"\nHas seleccionado la opción número 1.\n")
                print(f"La fórmula que vamos a utilizar es P = 2πr.\n")
                print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                radio = float(input(f"Introduce el radio de la circunferencia en {unidadSel}: "))
                resultado = float(round(2 * 3.1415 * radio * conversion, 2))
                print(f"\nEl perímetro de la circunferencia es de {resultado} {unidadSel}.\n")
            elif opcion == (2):
                print(f"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(f"\nHas seleccionado la opción número 2.\n")
                print(f"La fórmula que vamos a utilizar es P = 2πr.\n")
                print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                radio = float(input(f"Introduce el radio de la circunferencia en {unidadSel}: "))
                resultado = float(round(2 * 3.1415 * radio, 2))
                print(f"\nEl perímetro de la circunferencia es de {resultado} {unidadSel}.\n")
            repetir = int(input(f"¿Quieres realizar otra operación? (1. Si / 2. No / 3. Cambiar de unidades) "))
            if repetir == (1):
                menuPrincipal = True
            elif repetir == (3):
                print(f"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                menuUnidad = True
    elif opcion == (4):
        print(f"\nCerrando programa...\n")
        menuPrincipal = False
        exit
    else:
        input("\nLa opción seleccionada no existe. Por favor, vuelve a intentarlo. (Pulsa ENTER para reiniciar)")