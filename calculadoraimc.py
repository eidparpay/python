peso = float(input("Introduce tu peso en kg:"))
altura = float(input("Introduce tu altura en m:"))
altura = altura * altura
imc = float(peso / altura)

if (imc < 18.5):
    print ("Tu IMC tiene un valor de:", imc, "Usted tiene un bajo peso.")
elif (imc < 25):
    print ("Tu IMC tiene un valor de:", imc, "Usted tiene un peso saludable.")
elif (imc < 30):
    print ("Tu IMC tiene un valor de:", imc, "Usted tiene un sobrepeso.")
else:
    print ("Tu IMC tiene un valor de:", imc, "Usted tiene obesidad.")