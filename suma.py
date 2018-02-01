#coding: utf8
x=input("Introduzca un numero:")
i=0
suma=0
while (i<x):
	aux=input("Introduzca otro numero:")
	if aux>0:
		i+=1
		suma=aux+suma
print"La suma de numeros positivos es:",suma
print("Programa finalizado")
