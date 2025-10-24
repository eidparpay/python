# Haz un programa que realize la gestión de la introdución de un pin en un móvil


passwd = int(input("Configura un PIN para acceder al dispositivo: "))
passwdTry = int(0)
intentos = 3

while passwd != passwdTry:
    while intentos > 0:
        passwdTry = input("Introduce tu PIN: ")
        if passwdTry == passwd:
            print ("¡Bienvenido!")
        else:
            intentos = intentos - 1
            print (f"El PIN es incorrecto. Por favor, vuelva a intentarlo. Le quedan {intentos} intentos.")
            if intentos == 0:
                print ("Demasiados intentos incorrectos. Por favor, inténtelo de nuevo más tarde.")