#coding: utf8
num=input("Introduzca un numero entero:")
num1=input("Introduzca un numero igual o mayor que "+str(num)+":")
while (num > num1):
    print("¡Le he pedido un número entero mayor que "+str(num)+  "!")
    num1=input("Intentelo de nuevo:")

for i in range(num,num1+1):
    if i%2 ==0:
        print ("Este numero "+str(num)+" es par")
    if i%2 !=0:
        print ("Este numero "+str(num1)+" es impar")
print "Programa Terminado"
