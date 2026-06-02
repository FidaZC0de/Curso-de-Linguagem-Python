# Pedir primeiro numero pro usuário
# Pedir o segundo numero pro usuário 
# Pedir um operador (soma, subtração, multiplicação e Divisão)
# Depois pegar o primeiro numero e usar o operador com o segundo numero
# Utilizar While

while True:

 try:
    print("=" *100)
    print("Bem-Vindo à sua calculadora :) ")
    print("\nDigite 1 para realizar a operação de soma entre dois numeros (+) ")
    print("Digite 2 para realizar a operação de subtração entre dois numeros (-) ")
    print("Digite 3 para realizar a operação de multiplicação entre dois numeros (x) ")
    print("Digite 4 para realizar a operação de divisão entre dois numeros (%)")
    print("Digite 5 para sair da calculadora")
    print("=" * 100)
    opcao = int(input("Faça a sua escolha: "))
 except:
    print("Digite um numero válido !")
    print("Reiniciando Menu de Escolhas...")
    continue

 if opcao == 1:
     try:
        print("Operação ecolhida: Soma")
        numero_1 = float(input("\nDigite o primeiro numero: "))
        numero_2 = float(input("\nDigite o segundo numero: "))
        soma = numero_1 + numero_2
        print(f"Aqui está o resultado da operação de soma: {soma}")
     except:
      print('Você não digitou numeros válido')
      continue
       
 if opcao == 2:
     try:
       print("Operação escolhida: Subtração")
       numero_1 = float(input("\nDigite o primeiro numero: "))
       numero_2 = float(input("\nDigite o segundo numero: "))
       subtracao = numero_1 - numero_2
       print(f"Aqui está o resultado da operação de subtração {subtracao}")
     except:
        print('Você não digitou numeros válido')
        continue
 if opcao == 3:
     try:
       print("Operação escolhida: Subtração")
       numero_1 = float(input("\nDigite o primeiro numero: "))
       numero_2 = float(input("\nDigite o segundo numero: "))
       multiplicacao = numero_1 * numero_2
       print(f"Aqui está o resultado da operação de multiplicação: {multiplicacao}")
     except:
        print('Você não digitou numeros válido')
        continue
 if opcao == 4:
     try:
       print("Operação escolhida: Subtração")
       numero_1 = float(input("\nDigite o primeiro numero: "))
       numero_2 = float(input("\nDigite o segundo numero: "))
       divisao = numero_1 / numero_2
       print(f"Aqui está o resultado da operação {divisao}")
     except:
        print('Você não digitou numeros válido')
        continue
 if opcao == 5:
    print("Saindo da calculadora...")
    break



     
       
