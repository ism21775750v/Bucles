#coding: utf8
numero = int(input("Escriba un número entero mayor que 1: "))
while numero <= 1:
      numero= int(input(str(numero) + " no es mayor que 1. Inténtelo de nuevo: "))
factor  = numero

print("Descomposición en factores primos: ")
i = 2
while factor > i:
    while factor % i == 0:
        factor = factor // i
        print(i)
    i += 1
print(factor)

print("Esta es la descomposición factorial de el numero indicado.")
print("Programa terminado")
