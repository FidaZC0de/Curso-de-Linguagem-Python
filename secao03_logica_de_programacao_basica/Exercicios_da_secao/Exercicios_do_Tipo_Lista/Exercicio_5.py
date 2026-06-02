# 5. Peça 5 números ao usuário e exiba o maior e o menor — sem usar max() ou min().
import sys

contador = 1
num_list = []
maior = float("-inf")
menor = float("inf")

while contador <= 5:
    numbers = float(input("Digite um numero:  "))
    num_list.append(numbers)
    for numero in num_list:
        if numero > maior:
            maior = numero
            numero = maior
        if numero < menor:
            menor = numero
            numero = menor

    contador += 1

print(f"O maior numero dentre os numeros digitados eh o numero {maior} e o menor numero eh o numero {menor}")


