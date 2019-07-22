# Programa que capture 2 numeros enteros pedir numero mientras n1 no sea mayor que n2,imprimir numeros
n1=int(input("Digite número1: "))
n2=int(input("digite numero2: "))
while n1>=n2:
  n2=int(input("digite numero2: "))
print("el número menor es: ",str(n1))
print("el número mayor es: ",str(n2))
