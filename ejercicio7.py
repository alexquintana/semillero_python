numeros=list(eval(input("Digite 3 números al azar no consecutivos separados por comas: ")))
numeros.sort() #esta linea es para ordenar la lista original
for n in numeros:
    print(n)
