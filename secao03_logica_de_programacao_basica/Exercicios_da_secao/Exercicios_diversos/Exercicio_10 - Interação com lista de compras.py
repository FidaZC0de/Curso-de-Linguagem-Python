"""
Faça uma lista de compras com listas

O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista

Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista_de_compras = []

while True:
    try:
     print("-----\tBem-Vindo ao seu Menu de compras  -----")
     print("\tPara Inserir um item a sua lista de compras pressione 1")
     print("\tPara Apagar um item da sua lista de compras pressione 2")
     print("\tPara Listar os itens da sua lista de compras pressione 3")
     opcao = int(input("\nPressione o numero que corresponde com a ação desejado: "))
    except ValueError:
     print('Por favor digite número int.')
     continue

    if opcao == 1:
        os.system('cls')
        item = input("Digite o nome do que voce deseja inserir na sua lista de compras: ")
        lista_de_compras.append(item)
        print("O item foi adicionado a sua lista de compras :)")
        print(f"Sua lista de compras atual pós ação desejada: {lista_de_compras}") #Falta colocar em qual indice o item está
        continuar_no_sistema = input("Deseja continuar no sistema de compras ? (s/sim - para continuar/ n/nao - para sair do sistema)")
        if continuar_no_sistema == "s" or "sim":
           continue
        else:
           break
    elif opcao == 2:
     try:
        os.system('cls')
        item_a_ser_apagado = input("Digite o nome do item a ser apagado da sua lista de compras: ")
        lista_de_compras.remove(item_a_ser_apagado)
        print("O item foi apagado da sua lista de compras :)")
        print(f"Sua lista de compras atual pós ação desejada: {lista_de_compras}") # Mostrar a lista com os indices
     except:
        print("Esse item não está na sua lista de compras ! ")
     continue
    
    if continuar_no_sistema == "s" or "sim":
           continue
    else:
     break
    
    #Falta Organizar o Pylance
    elif opcao == 3:
    os.system('cls')
    print("Listando lista de compras...")
    print(f"Sua lista de compras {lista_de_compras}") #Mostrar a lista com os indices
    if continuar_no_sistema == "s" or "sim":
     continue
    else:
     break


        



