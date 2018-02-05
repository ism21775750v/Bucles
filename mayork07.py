#coding: utf8
x=input("Escriba un numero:")
z=input("Escriba el un numero mayor que "+str(x)+":")
y=input("Escriba un número entre "+str(x)+" y "+str(z)+":" ) 
cont=0
while(x>=z):
		print str(y)+"no es mayor que "+str(x)+"."
		z=input("Inténtelo de nuevo:")
while (y>x) and (y<z): 
                y=input("Escriba un número entre "+str(x)+" y "+str(z)+":" )
		cont=+1
print "Has escrito "+str(cont)+" números  entre "+str(x)+" y "+str(z)
print "Programa Terminado"
		
