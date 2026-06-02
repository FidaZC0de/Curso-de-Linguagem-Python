'''Peça ao usuário dois valores para serem comparados e fazer com que o maior valor seja impresso primeiro '''

valor_1 = float(input("Digite o primeiro valor para a comparação: "))

valor_2 = float(input("Digite o segundo valor para a comparação"))

if valor_1 > valor_2:
    print(f"O primeiro valor inserido {valor_1} eh maior do que o segundo valor inserido, o {valor_2}")
else:
    print(f"O segundo valor a ser inserido {valor_2}, eh maior do que o primeiro valor insirido, o {valor_1}")