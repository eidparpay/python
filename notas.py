nota = float(input("¿Qué nota has sacado en el examen?"))
if nota < 5:
    print("Tu nota es ", nota, ". Tienes un insuficiente.")
elif nota < 6:
    print("Tu nota es ", nota, ". Tienes un suficiente.")
elif nota < 7:
    print("Tu nota es ", nota, ". Tienes un bien.")
elif nota < 9:
    print("Tu nota es ", nota, ". Tienes un notable.")
elif nota < 10:
    print("Tu nota es ", nota, ". Tienes un excelente.")
elif nota == 10:
    print("Tu nota es ", nota, ". Tienes una matrícula de honor.")
else:
    print("Has introducido incorréctamente la nota del examen. Vuelve a introducir la nota.")
    nota = float(input("¿Qué nota has sacado en el examen?"))