# 4. Crie uma lista de nomes e exiba somente os que têm mais de 4 letras.

names_list = ["Marco", "Luiz", "Sabrina", "João", "Yuri", "Jorge", "Valentina"]

for name in names_list:
    if len(name) >= 5:
        print(name)