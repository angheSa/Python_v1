# calculadora, + - * /

print("Ingrese el primer numero")
a = int(input())
print("Ingrese otro número")
b = int(input())
print("¿Que desea hacer?")
print("1 - Sumar")
print("2 - Restar")
print("3 - Multiplicación")
print("4 - División")
operacion = int(input())

if operacion == 1 :
    print("Su resultado es: ", a + b)
elif operacion == 2 :
    print("Su resultado es: ",a - b)
elif operacion == 3 :
    print("Su resultado es: ",a * b)
else :
    print("Su resultado es: ",a / b)