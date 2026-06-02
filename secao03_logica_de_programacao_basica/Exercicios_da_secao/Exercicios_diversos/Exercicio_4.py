'''Peca ao usuario para para digitar seu nome 
   Peca ao usuario para digitar a sua idade 
   Se nome e idade forem digitados:
   Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém {n} letras
        A primeira letra do seu nome é {letra}
        A ultima letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos importantes vazios."

'''

nome_usuario = str(input("Digite o seu nome: "))
idade_usuario = (input("Digite a sua idade: "))

tamanho_nome = len(nome_usuario)


if nome_usuario and idade_usuario:
    print(f"Seu nome {nome_usuario} :) ")
    print(f"Seu nome invertido eh {nome_usuario[::-1]}")
    print(f"Seu nome comtém {tamanho_nome} letras :) ")
    print(f"A primeira letra do seu nome é a letra {nome_usuario[0]}")
    print(f"A ultima letra do seu nome eh a letra {nome_usuario[-1]}")
else:
    print("Desculpe, você deixou campos importantes vazios.")


