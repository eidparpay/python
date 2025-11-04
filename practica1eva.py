# Programa para realizar cálculos matemáticos con 3 MENÚS funcionales y conversión de hasta 4 UNIDADES diferentes.

# Declaramos las variables que utilizaremos para realizar los menús (utilizando únicamente los comandos que hemos aprendido hasta ahora),
# las unidades que tenemos permitidas utilizar y el resultado de la conversión de unidades.

menuPrincipal = True
menuUnidad = False
unidadPer = ['mm', 'cm', 'm', 'km']
conversion = float(1)

# Creamos el primer bucle donde se encontrará todo el programa del cual constará el primer menú con las distintas opciones disponibles.
while menuPrincipal == True:
    print(f"\n\n\n\n\n~~~ CÁLCULO MATEMÁTICO ~~~\n")
    print(f"Selecciona una de las siguientes opciones...\n")
    print(f"1. Cálculo del perímetro de una circunferencia de radio r.")
    print(f"2. Cálculo del área de un círculo de radio r.")
    print(f"3. Cálculo del volumen de una esfera de radio r.")
    print(f"4. Salir del programa.\n")
    print(f"~~~~~ /\+/\-/\*/\^/\ ~~~~~\n")
    # Preguntamos la opción que queremos realizar.
    opcion = (int(input("Inserta número de opción: ")))
    # Si la opción NO es salir del programa, continuaremos preguntando las unidades.
    if opcion == 1 or opcion == 2 or opcion == 3:
        menuUnidad = True
        # Creamos el segundo bucle donde se preguntarán las unidades con las que se quiera trabajar.
        while menuUnidad == True:
            unidadSel = (input(f"\nEscribe las unidades con las que quieres trabajar (mm, cm, m, km): "))
            # Si la unidad no existe, el programa avisará al usuario y volverá a preguntarle la unidad con la que quiere trabajar.
            if unidadSel not in unidadPer:
                input("\nLa unidad seleccionada no existe. Por favor, vuelve a intentarlo. (Pulsa ENTER para volver a introducir la unidad)")
            else:
                # Como la unidad sí que existe, quitamos la posibilidad de que el programa esté constantemente repitiéndose.
                menuUnidad = False
                menuPrincipal = False
                menuUnidadCon = True
                # Creamos el tercer bucle donde se preguntarán las unidades a las que el usuario quiere convertir el resultado.
                while menuUnidadCon == True:
                    unidadSelCon = (input(f"\nEscribe las unidades a las que quieras convertir (mm, cm, m, km): "))
                    # Si la unidad no existe, el programa avisará al usuario y volverá a preguntarle la unidad a la que quiere convertir el resultado.
                    if unidadSelCon not in unidadPer:
                        input("\nLa unidad seleccionada no existe. Por favor, vuelve a intentarlo. (Pulsa ENTER para volver a introducir la unidad)")
                    else:
                        # Realizamos la conversión de unidades, multiplicando o dividiendo por/entre 10 dependiendo de la cantidad de ceros que hay entre cada unidad permitida.
                        # Por ejemplo: (1 m = 1.000 mm) (1 km = 100.000 cm)
                        if unidadSel == "mm":
                            valorUnidad = 0
                        elif unidadSel == "cm":
                            valorUnidad = 2
                        elif unidadSel == "m":
                            valorUnidad = 4
                        elif unidadSel == "km":
                            valorUnidad = 7
                        if unidadSelCon == "mm":
                            valorUnidadCon = 0
                        elif unidadSelCon == "cm":
                            valorUnidadCon = 2
                        elif unidadSelCon == "m":
                            valorUnidadCon = 4
                        elif unidadSelCon == "km":
                            valorUnidadCon = 7
                        # Cuando las unidades sean diferentes, el programa realizará la conversión de unidades.
                        while valorUnidad != valorUnidadCon:
                            if valorUnidadCon > valorUnidad:
                                conversion = float(conversion / 10)
                                valorUnidad = valorUnidad + 1
                            elif valorUnidadCon < valorUnidad:
                                conversion = float(conversion * 10)
                                valorUnidad = valorUnidad - 1
                        menuUnidadCon = False 
            # Si la opción es la Nº1, realizaremos el perímetro de una circunferencia con la fórmula indicada.     
            if opcion == (1):
                print(f"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(f"\nHas seleccionado la opción número 1.\n")
                print(f"La fórmula que vamos a utilizar es P = 2πr.\n")
                print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                radio = float(input(f"Introduce el radio de la circunferencia en {unidadSel}: "))
                resultado = float(round(2 * 3.1415 * radio * conversion, 10))
                print(f"\nEl perímetro de la circunferencia es de {resultado} {unidadSelCon}.\n")
            # Si la opción es la Nº2, realizaremos el área de un círculo con la fórmula indicada.     
            elif opcion == (2):
                print(f"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(f"\nHas seleccionado la opción número 2.\n")
                print(f"La fórmula que vamos a utilizar es A = πr².\n")
                print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                radio = float(input(f"Introduce el radio del círculo en {unidadSel}: "))
                resultado = float(round(3.1415 * (radio * conversion) ** 2, 10))
                print(f"\nEl área del círculo es de {resultado} {unidadSelCon}².\n")
            # Si la opción es la Nº3, realizaremos el volumen de una esfera con la fórmula indicada.     
            elif opcion == (3):
                print(f"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(f"\nHas seleccionado la opción número 3.\n")
                print(f"La fórmula que vamos a utilizar es V = 4/3*πr³.\n")
                print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                radio = float(input(f"Introduce el radio de la esfera en {unidadSel}: "))
                resultado = float(round((4 / 3) * 3.1415 * (radio * conversion) ** 3, 10))
                print(f"\nEl volumen de la esfera es de {resultado} {unidadSelCon}³.\n")
            # Cuando el problema está resuelto, preguntaremos al usuario si quiere continuar con otra operación del programa, cambiar las unidades o salir del mismo.
            repetir = int(input(f"¿Quieres realizar otra operación? (1. Si / 2. No / 3. Cambiar de unidades) "))
            if repetir == (1):
                menuPrincipal = True
            elif repetir == (3):
                print(f"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                menuUnidad = True
            elif repetir == (2):
                print(f"\nCerrando programa...\n")
                exit
    # Si la opción es salir del programa, nos saldrá un mensaje y cerrará el programa.
    elif opcion == (4):
        print(f"\nCerrando programa...\n")
        menuPrincipal = False
        exit
    # Si la opción no existe, volverá a preguntar al usuario que ingrese una opción.
    else:
        input("\nLa opción seleccionada no existe. Por favor, vuelve a intentarlo. (Pulsa ENTER para reiniciar)")