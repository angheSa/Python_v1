
# len() , saber la longitud de una cadena

my_name = "Maria Sandoval Pilar"
print(len(my_name))

# tabulacion \t y salto de linea \n
phrase = "\tMañana viajaré a Brasil\n\tElla viaja mañana"
print(phrase)

"""""
Old style string formatting: 
%s - string
%d - integers
%f  - float  
Para referenciarlos : %(var1,var2,var3)

"""
name = "Juan"
lastname = "Perez"
age = 34
print("Mi nombre es %s , mi apellido es %s y mi edad es %d " %(name, lastname, age))

"""""
New style string formatting ( version py 3)

{} - cualquier tipo de dato
para referenciarlos : .format(var1,var2,var3)

"""
product = "mirror"
category = "other things"
print ("The product is a {} and belongs to the category {}" .format(product,category))

"""""
another form is with string interpolation , strings start with f
"""
print(f"Mi nombre es {name} , mi apellido es {lastname} y mi edad es {age}")

"""""
python strings as sequences of characters

"""

#unpacking characters
letters = "Monica"
x, y,z,c,d,m = letters
print(x, y, z)

first_letter = letters[0]
print(first_letter)

last_three = letters[3:5]
print(last_three)

last_three_right = letters[-3:]
print(last_three_right)


#start from right. -1
from_right_zero = len(letters) -1
new_from = letters[from_right_zero]
print(new_from)
from_right = letters[-1]
print(from_right)
from_right_two = letters[-4]
print(from_right_two)


#reversing a string
reverse_one = letters[::-1]
print(reverse_one)

#methods
phrase_two = "La vida es bella"
print(phrase_two.upper())
print(phrase_two.lower())
print(phrase_two.count('a'))
print(phrase_two.count('la'))
print(phrase_two.count('a', 3 , 7))
print(phrase_two.capitalize()) # la primera letra lo vuelve en mayuscula
print(phrase_two.endswith('a')) # devuelve true o false si cumple la coincidencia propuesta.
print(phrase_two.endswith('bella'))
print(phrase_two.find('a')) # te devuelve la primera posicion en la cual se encuentre la coincidencia
print(phrase_two.rfind('a')) # te devuelve la ultima posicion en la cual se encuentre la coincidencia
print(phrase_two.index('a'))
print(phrase_two.islower()) ## funciona como una condicional, te vuelve true o false si se cumple esa funcion(creo que funciona en todos los is)
print(phrase_two.isupper()) #false
print(phrase_two.startswith('L')) # devuleve true o false si inicia con la ocurrencia
print(phrase_two.replace("vida" , "luna")) # reemplaza un substring por una cada dada
print(phrase_two.isalpha()) #devuelve true o false si tiene caracteres, no se considera al espacio como caractere
alpha_true = "Maria"
print(alpha_true.isalpha()) #devuelve true o false si tiene caracteres, no se considera al espacio como caractere

