#coding: utf-8
num1=input("Introduzca un numero:")
num2=input("Introduzca un numero mayor que" +str(num1)+":")

while (num1<=num2):
	num1=num2
	num2=input("Introduzca un numero mayor que" +str(num1)+":")
print num2 ,"no es mayor que", num1
	
