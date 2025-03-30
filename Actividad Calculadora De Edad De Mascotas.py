tipo = input("¿Tu mascota es un perro o un gato?: ").lower()
edad = int(input("Ingresa la edad de tu mascota: "))

if tipo == "perro":
    edad_humana = edad * 7
    print("La edad de tu perro en años humanos es:", edad_humana)
elif tipo == "gato":
    edad_humana = edad * 5
    print("La edad de tu gato en años humanos es:", edad_humana)
else:
    print("Solo puedo calcular para perros o gatos.")