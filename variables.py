"""""
En python se puede cambiar y forzar el tipo de dato

"""

numberOne = 23
textOne = "Girasoles"
print(numberOne,textOne)

numberOne = "Muriel"
textOne = 34
print(numberOne,textOne)
print(type(numberOne),type(textOne))

# También se puede declarar varias variables en una sola linea

nombre, apellido, edad = "Martin" , "Gonza" ,  23
print(nombre,apellido, "Mi ead es: ",edad)