import random

# Generar el código secreto con 5 claves aleatorias y expresiones matemáticas
codigo_secreto = {
    random.randint(1, 20): "5 + 4 - 6",
    random.randint(1, 20): "3 * 3 - 2",
    random.randint(1, 20): "10 // 5",
    random.randint(1, 20): "8 + 1",
    random.randint(1, 20): "16 // 4"
}

# Mostrar el desafío al usuario
print("Descifra el código secreto respondiendo las siguientes operaciones:")

# Validación de las respuestas del usuario
aciertos = 0
for clave, expresion in codigo_secreto.items():
    respuesta_correcta = eval(expresion)  # Evalúa la expresión matemática
    respuesta_usuario = int(input(f"¿Cuánto es {expresion}? "))

    if respuesta_usuario == respuesta_correcta:
        aciertos += 1
    else:
        print("Acceso Denegado")
        break  # Si se equivoca en alguna, termina el juego

# Resultado final
if aciertos == len(codigo_secreto):
    print("¡Código Descifrado!")