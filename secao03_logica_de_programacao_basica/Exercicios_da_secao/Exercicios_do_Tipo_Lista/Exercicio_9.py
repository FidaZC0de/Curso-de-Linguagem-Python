# Dada a lista [4, 7, 2, 7, 1, 4, 9, 2, 6, 9], crie uma nova lista
# com os mesmos números mas sem repetições, mantendo a ordem original
# — sem usar set().

lista = [4, 7, 2, 7, 1, 4, 9, 2, 6, 9]

nova_lista = []

print(f"Lista Antes {lista}")

for numero in lista:
    if numero not in nova_lista:
        nova_lista.append(numero)   

print(f"lista Depois {nova_lista}") 