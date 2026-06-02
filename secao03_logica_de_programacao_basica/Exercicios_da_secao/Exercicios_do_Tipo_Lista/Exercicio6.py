# 7. Inverta uma lista sem usar .reverse() ou [::-1].

list_to_invert = [1,2,3,4,5,6,7,8,9,10]

print(f"Lista antes da inversão: {list_to_invert}")

inverted_list = []

for indice in range(len(list_to_invert) - 1, -1, -1):
    inverted_list.append(list_to_invert[indice])

print(f"Lista pós inversão: {inverted_list}")

#----------------------------------------------------------------------------------
    



        