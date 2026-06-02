# 2. Peça ao usuário para digitar 5 números, guarde numa lista e exiba a soma total.


lista_numeros = []
contador = 0
soma = 0

while contador <= 4:
 soma += 1
 numero = int(input("Digite um numero: "))
 lista_numeros.append(numero)
 soma = sum(lista_numeros)
 contador += 1

print(f"Lista de numeros preenchida por você --> {lista_numeros}")

