# crearemos un programa que calcule la suma desde el numero 1 hasta el 
# numero ingresado por el usuario
n = input("Por favor ingresa un numero entero:")

# usamos una condicional para verificar que el numero sea entero 
if n.isdigit():
    
    n = int(n)
    
    suma = 0
    i = 0  
    
    while i <= n:
        suma = suma + i 
        i =  i + 1 
    
    # al salir imprimos los resultados 
    print("La suma de los primeros",n,"numeros es de:",suma)
    
else:
    print("Error solo se permite ingresar numeros enteros:")
    