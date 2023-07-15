# List : Ordenada, modificable, permite miembros duplicados

my_list = list("Maria")
print(my_list) ## devuelve los valores del elemento que está dentro ,('M', 'a', 'r', 'i', 'a')

my_list_two = ["Juan", "Muria", "Oscar",23,True]
print(my_list_two)
print(len(my_list_two))
my_list_three =["Mariana", "Dylan", "Andrés"]
print(my_list_three)
print(my_list_three[2])
print(my_list_three[0:2])
print(my_list_three[-1])
#methods
list_four = ["A", "J", "Z", "D"]
list_four.append("J") # inserta al último un nuevo valor
print(list_four)
list_four.insert(1,"Z") # insertas un valor según la posición indicada 
print(list_four)
list_four.remove("Z") # eliminas el valor indicado, acepta str
print(list_four)
list_four.pop(0) # elimina segun el indice, y si no se especifica pues se elimina el ultimo elemento
#print(list_four.pop(4)) # te muestra el valor eliminado segun el indice
print(list_four)
print(list_four.count("A")) # devuelve la cantidad de ocurrencias del valor indicado
list_four.sort() # ordena la lista de forma ascendente
print(list_four)
new_list = list_four.copy()# copiar toda la lista a otra variable
print("The new list: ", new_list)
#modificando la nueva lista, no se altera la lista antigua
new_list.append("P")
print(new_list)

new_list.reverse() # voltea la lista
print(new_list)
##new_list.clear() # elimina todos los elementos de la lista
del new_list[2] # eliminas segun el indice, segun un rango [2:3] o toda la lista
print(new_list)

# devuelve el indice del item, si existe dos, te devuelve la primera posicion de la ocurrencia
print(new_list.index("J") )
"""""
Para concatenar una lista se puede usar +
o también extend()
"""
## unes todo y lo guardas en una variables
lista1 = [1,2,3,4]
lista2 = [2,5,67,8]
unir_lista = lista1 + lista2
print(unir_lista)

# solo extiendes a la lista 1, se imprimirá todo cuando invoques a la lista 1
# si invocas a la lista2 solo te devovlerá los elementos de la lista2
lista1.extend(lista2)
print(lista1)

##Validar que existe un elemento en una lista , devulve true or false
result = "m" in lista1  #RETURN FALSE
print(result)
