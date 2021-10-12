limite = int(input("ingrese el limite "))
suma_pares = 0
suma_impares = 0
for x in range(limite):
    number = int (input("ingrese el numero "))
    if number % 2 == 0:
        suma_pares+=number
    else:
        suma_impares+=number
print("la suma de los pares es: ",suma_pares)
print("la suma de los impares es: ",suma_impares)


