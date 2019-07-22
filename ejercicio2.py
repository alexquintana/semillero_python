#Escriba un programa que pida números decimales mientras el usuario escriba numeros mayores que el primero
n1=float(input("Digite un número: "))
n2=float(input("Digite un número: "))
while n2>=n1:
  n2=float(input("Su numero es: "+str(n2)+" ,\n vuelva a digitar el número: "))
print("Su número digitado es: "+ str(n2)+"  \t es menor que: "+ str(n1))
