lista1 = [1,3,5,7,9]
lista2 = [2,1,4,3,6,5,8,7,10,9]
lista3 = []

for elemento in lista1:
    if elemento in lista3:
        print(f"o valor {elemento} já existe na lista")
    else:
        lista3.append(elemento)

for elemento in lista2:
    if elemento in lista3:
        print(f"o valor {elemento} já existe na lista")
    else:
        lista3.append(elemento)

for x in range(len(lista3)):
    print(f"Elemento {x} = {lista3[x]}")