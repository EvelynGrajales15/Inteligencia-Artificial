cuenta = float(input("Ingresa el total de tu cuenta: "))
propina = int(input("¿Qué porcentaje de propina quieres dejar? (10, 15, 20): "))

if propina == 10:
    total = cuenta * 1.10
elif propina == 15:
    total = cuenta * 1.15
elif propina == 20:
    total = cuenta * 1.20
else:
    print("Porcentaje no válido, se aplicará 0% de propina.")
    total = cuenta

print("El total a pagar es:", total)