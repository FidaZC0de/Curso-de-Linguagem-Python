# Peça um número ao usuário e imprima a tabuada dele.

interacao_num = int(input("Digite um numero --:> "))
numeros = range(1, 11)

for numero in numeros:
     res_multi = interacao_num * numero
     print(f"{interacao_num} x {numero} = {res_multi}")









