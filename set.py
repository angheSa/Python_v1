""""
Set(CONJUNTO): desordenada, no indexada, inmutable(solo permite agregar,eliminar,update elementos nuevos) y no elementos duplicados.
"""
## devuelve los valores del elemento que está dentro {'a', 'r', 'M', 'i'}
## no devuelve dos veces "a" porque no acepta duplicadps, y devuelve lista desordenada
set_new = set("Maria")
print(set_new)

## set con valores definidos  con LLAVES
set_new_two = {2,3.3,"Maria", True}
print(set_new_two)

#puedes obtener la longitun, cantidad de elementos
print(len(set_new_two))

# puedes validar si existe o no un elemento
result = 2 in set_new_two
print(result)

# agregar un valor o varios valores
# ten en cuenta que no añade valores repetidos

set_new_three = {1,4,3,2,6}
set_new_three.add(9)
print(set_new_three)

set_new_three.update([8,12,13,14]) # agregando varios items
print(set_new_three)

ejemplo2 = {20,21,22}
set_new_three.update(ejemplo2)
print(set_new_three)

## eliminar un item
set_new_three.remove(20)
print(set_new_three)

## eliminar un item random, y tbm devuelve el elemento eliminado

ejemplo2.pop()
print(ejemplo2)

## borramos los elementos
ejemplo2.clear()
print(ejemplo2)

## borramos todo el set
del ejemplo2

## también se puedeconvertir en list y un list en tupla

## se puede unir tuples con join