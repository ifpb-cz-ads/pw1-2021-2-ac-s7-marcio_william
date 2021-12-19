lista1 = [1,2,3,4]
lista2 = [5,6,7,8,9,10]
lista3 = []

for elemento in lista1:
    lista3.append(elemento)

for elemento in lista2:
    lista3.append(elemento)

for x in range(len(lista3)):
    print(f"Elemento {x} = {lista3[x]}")