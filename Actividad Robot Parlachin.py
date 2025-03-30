# programa 1 robot parlachin 

while True:
    mensaje = input("Escribe algo: ")
    
    if mensaje == "Hola":
        print("¡Hola humano!")
    elif mensaje == "Adiós":
        print("¡Hasta luego, terrícola!")
        break  # Termina el programa si el usuario dice "Adiós"
    else:
        print("No entiendo, intenta de nuevo.")
