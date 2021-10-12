sumapar=0
sumaimpar=0
limite=int(input("Ingrese el límite: "))
for i in range(limite):
    number=int(input("Ingrese un número: "))
    if number % 2 ==0:
        sumapar += number
    else:
        sumaimpar += number
print("La suma de los pares es ",sumapar)
print("La suma de los impares es ",sumaimpar)



