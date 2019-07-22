l=int(input("Digite su límite positivo: "))
while l<0:
  print("El número digitado debe ser positivo.")
  l=int(input("digite su número limite entero positivo: "))
n1=int(input("digite un número: "))
n2=0
while n1<l:
  n2=int(input("Digite un número: "))
  n1=n1+n2
print("La suma de los números supero el límite digitado: ",n1)
