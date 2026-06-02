# Iterando strings com while

# """
#       012345678910
# nome = 'Luiz Otávio'  # Iteráveis
# #      1110987654321
# tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)
# print(nome[3])

# nova_string = ''
# nova_string += '*L*u*i*z* *O*t*á*v*i*o'


cpf = "12345678910"  # Iteráveis

indice = 0
novo_cpf = ''

while indice < len(cpf): #O while vai fazer o loop de acordo com o tamanho da String cpf
    numero = cpf[indice]
    
    if indice == 3 or indice == 6:
        novo_cpf += '.'

    if indice == 9:
        novo_cpf += '-'

    novo_cpf += numero
    indice += 1

print(novo_cpf)





