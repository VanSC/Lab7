numeros_impares=0
numeros_pares=0
suma=0
for x in range(6):
        number=int(input("ingrese numero "))
        if number % 2 == 0:
            numeros_pares+=1
        else:
            numeros_impares+=1
print("la cantidad de numeros impares es: ",numeros_impares)
print("la cantidad de numeros pares es: ",numeros_pares)
