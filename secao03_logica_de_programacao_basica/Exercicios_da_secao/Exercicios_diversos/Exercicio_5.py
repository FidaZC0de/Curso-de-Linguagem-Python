"""Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
print("-----Questão 1 da Lista-----")
try:
    numero_digitado = int(input("\nDigite um numero (Inteiro) : ")) #Peço o numero 
    if numero_digitado % 2 == 0: # Checa se o numero eh par
     print("O numero que voce digitou é Par !")
    elif numero_digitado % 2 != 0: #Checa se o numero eh impar
     print("O numero que voce digitou eh Ímpar")

except: # O erro que der dentro do try cai no except
    print("Voce nao digitou um numero inteiro !!!")


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
print("-----Questão 2 da Lista-----")
horario = int(input("\nOlá, Digite o que horas são (com numeros inteiros e entre 0 e 23) : "))

if horario >= 0 and horario <= 11:
   print("Bom dia !")
elif horario >= 12 and horario <= 17:
   print("Boa Tarde !")
else:
   print("Boa noite !")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

print("-----Questão 3 da Lista-----")
nome = str(input("Digite o seu nome: "))

if len(nome) <= 4:
   print("O seu nome é curto")
elif len(nome) >= 5 and len(nome) <= 6:
   print("O seu nome é normal !")
elif len(nome) > 6:
   print("O seu nome é muito grande !")
   
   