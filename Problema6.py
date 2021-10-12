pares=0
impares=0
neutro=0
negativos=0
positivos=0
limite=5
for x in range(limite):
    number=int(input("ingres el numero "))
    if number % 2 == 0:
        pares+=1
    else:
        impares+=1
    if x<0:
        negativos+=1
    else:
        positivos+=1
    if number == 0:
        neutro = 0
print("La cantidad de numeros pares es: ",pares)
print("La cantidad de numeros impares es: ",impares)
print("La cantidad de numeros negativos es: ",negativos)
print("La cantidad de numeros positivos es: ",positivos)
print("El numero neutro es: ",neutro)