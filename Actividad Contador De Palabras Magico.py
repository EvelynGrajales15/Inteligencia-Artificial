frase = input("Escribe una frase: ")
palabras = frase.split()  # Divide la frase en palabras

contador = 0
for palabra in palabras:
    contador += 1  # Cuenta cada palabra

print("La frase tiene", contador, "palabras.")