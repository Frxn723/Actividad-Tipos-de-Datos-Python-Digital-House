print("Actividad 01 tipos de datos - Errores")
print()

# --- ERROR 1 ---
# Queremos saber el total de la suma de los números a y b.
numA = 2
numB = 3

total = numA + numB
print(total)

# --- ERROR 2 ---
# Queremos mostrar por consola el sabor de helado ingresado por el usuario.
sabor = str(input("Ingrese su sabor de helado favorito: "))
print("El sabor ingresado por consola es: " + sabor)

# --- ERROR 3 ---
# Queremos mostrar por consola el total de la multiplicación de dos números, numA y numB

numA = int(input("Ingrese número A: "))
numB = int(input("Ingrese número B: "))
resultado = str(numA * numB)

print("El resultado es:  " + resultado)

# Fin de la actividad 01

print()
print("Actividad 02 tipos de datos - Edad")

edad = int(input("Tu edad"))

edadFutura = str(edad + 18)

print("Tu edad dentro de 18 años será:" + "" + edadFutura)
