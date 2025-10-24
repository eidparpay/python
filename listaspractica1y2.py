# Haz un programa en Python que pida una contraseñla y no termine hasta que se escriba correctamente la contraseña. La contraseña será fijada por el propio programa.
# Amplia el programa anterior para qeu solo dé 3 oportunidades para introducirla y que genere un informe sobre ello.

passwd = input("Configura una contraseña para acceder al dispositivo: ")
passwdTry = ("prueba")
intentos = 3

while passwd != passwdTry:
    while intentos > 0:
        passwdTry = input("Introduce tu contraseña: ")
        if passwdTry == passwd:
            print ("¡Bienvenido!")
        else:
            intentos = intentos - 1
            print (f"La constraseña es incorrecta. Por favor, vuelva a intentarlo. Le quedan {intentos} intentos.")
            if intentos == 0:
                print ("Demasiados intentos incorrectos. Por favor, inténtelo de nuevo más tarde.")