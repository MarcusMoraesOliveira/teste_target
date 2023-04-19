numero = int(input("numero a ser procurado\n"))

fibonacci = [0,1]

while(fibonacci[-1] < numero):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])


if numero in fibonacci:
    print ("O numero " + str(numero) + " está na lista")
else:
    print ("O numero " + str(numero) + " não está na lista")