#coding: utf8
num=input("Introduzca un numero mayor que 0:")

while (num<0):
    print"¡Le he pedido un número entero mayor que 0!"
    num=input("Intentelo de nuevo:")
for i in range(1,num+1):
    if  num%i ==0:
        print (i)
