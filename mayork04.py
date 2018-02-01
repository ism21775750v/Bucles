#coding: utf8
x=input("Introduzca un numero:")
i=0
r=0

while (i<x):
	aux=input("Introduzca otro numero:")
	r+=1
	if aux>0:
		i+=1
print "Has escrito",r,"numeros,",i,"de ellos positivos."

