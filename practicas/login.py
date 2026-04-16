usuario_correcto = "cristobal"
password_correcta = "admin123"
intentos = 3
acceso = False # Esta es una "bandera" (boolean)

while intentos > 0 and acceso == False:
    
    verificar_usuario = input("Ingrese un usuario: ")
    
    if verificar_usuario == usuario_correcto:
        print("Usuario correcto")
        ingreso = input("Ingrese la contraseña: ").lower().strip()
        
        if ingreso == password_correcta: 
            acceso = True
        else:
            intentos -= 1
            print(f"Contraseña incorrecta. Te quedan {intentos} intentos.")    
    else:
        intentos -= 1
        print(f"Usuario incorrecta. Te quedan {intentos} intentos.")

# Al salir del bucle, hay que chequear por qué salió
if acceso == True:
    print("¡Acceso concedido!")
else:
    print("Sistema bloqueado por seguridad.")