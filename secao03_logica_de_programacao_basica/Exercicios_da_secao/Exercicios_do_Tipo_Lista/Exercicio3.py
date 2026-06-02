# 3. Dada a lista [3, 1, 4, 1, 5, 9, 2, 6], exiba apenas os números pares.

lista = [3, 1, 4, 1, 5, 9, 2, 6]

for numero in lista:
    if numero % 2 == 0:
        print(f"Numeros Pares da lista --> {numero}")