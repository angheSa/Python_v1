# Tupla : Ordenada, inmutable (no se puede modificar sus elementos), permite miembros duplicados
tupla2 = tuple("Maria")
print(tupla2) ## devuelve los valores del elemento que está dentro ,('M', 'a', 'r', 'i', 'a')
#para insertar varios valores predefinidos:
tupla1 = ("Maria", "Jose", "Luna",1,2,3) 
print(tupla1)

print(len(tupla1)) # saber la cantidad de elementos
#Se puede obtener los valores por intervalo y solo.
print(tupla1[0])
print(tupla1[-2])
print(tupla1[0:2])

## saber si existe o no tal item en una tupla
result = "Jose" in tupla1
print(result)

## para unir tuplas se puede usar +
new_tupla = tupla1 + tupla2

## para eliminar tuplas se usa del , no elimina solo un item, sino todo

del tupla1

## PARA MODIFICAR ALGÚN ITEM DE UNA TUPLA, SE DEBERÁ PASAR LA TUPLA A UN LIST()

tupla3 = (1,2,4,5,6,7,7)
new_list = list(tupla3)
print(new_list)
new_list.append(1)

print(new_list)