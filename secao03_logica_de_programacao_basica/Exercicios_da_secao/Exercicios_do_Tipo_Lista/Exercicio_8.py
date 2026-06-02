#  Crie uma lista com 8 números inteiros (misture positivos e negativos).
# # Exiba apenas os números que são positivos E ímpares.

lista_num = [1,2,-3,-4,5,-6,-7,-8]

for numero in lista_num:
    if numero > 0:
        print(f"\t{numero}")
    if numero % 2 != 0:
        print(f"\t{numero}")
    
    

