numeroUno = 0
numeroDos = 7
numeroTres = 25

# Paso 1
# Paso 1.1 - Pedir el primer número
textoUno = input("Ingrese el primer número: ")
numeroUno = float(textoUno)

# Paso 1.2 - Pedir el segundo número
textoDos = input("Ingrese el segundo número: ")
numeroDos = float(textoDos)

# Paso 1.3 - Pedir el tercer número
textoTres = input("Ingrese el tercer número: ")
numeroTres = float(textoTres)

# Paso 2
# Paso 2.1 - Sumar los números
suma = numeroUno + numeroDos + numeroTres
sumaFormato = "{:.2f}".format(suma)

# Paso 2.2 - Multiplicar los números
multiplicacion = numeroUno * numeroDos * numeroTres
multiplicacionFormato = "{:.2f}".format(multiplicacion)

# Paso 3
# Paso 3.1 - Mostrar el resultado de la suma
print(f"El resultado de la suma es: {sumaFormato}, y el resultado de la multiplicación {multiplicacionFormato}")
print("El resultado de la suma es: ", suma, ", y el resultado de la multiplicación ", multiplicacion)
# Paso 3.2 - Mostrar el resultado de la multiplicación
# print("El resultado de la multiplicación es: ", multiplicacion)
