# Some todos os números de 1 a 100 e exiba o resultado.

numeros = range(0, 101)
soma = 0

for numero in numeros:
    print(numero)
    soma += numero
   

print(f"Soma total de todos os numeros de 1 a 100 --> {soma}")