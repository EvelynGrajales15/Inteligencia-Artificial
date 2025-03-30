import random

while True:
    usuario = input("Elige piedra, papel o tijera (o escribe 'salir' para terminar): ").lower()

    if usuario == "salir":
        print("¡Gracias por jugar!")
        break

    if usuario not in ["piedra", "papel", "tijera"]:
        print("Opción no válida, intenta de nuevo.")
        continue

    computadora = random.choice(["piedra", "papel", "tijera"])
    print("La computadora eligió:", computadora)

    if usuario == computadora:
        print("¡Empate!")
    elif (usuario == "piedra" and computadora == "tijera") or (usuario == "papel" and computadora == "piedra") or (usuario == "tijera" and computadora == "papel"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")
