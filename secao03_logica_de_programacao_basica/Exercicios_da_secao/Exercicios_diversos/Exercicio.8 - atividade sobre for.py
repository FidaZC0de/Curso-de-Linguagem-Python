"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.

"""
import os

secret_word = "katana"
letras_acertadas = ""
num_try = 0

while True:

    try:
        try_letra = input(
            "Faça sua tentativa e digite apenas uma letra --> "
        ).lower()

        # valida se digitou apenas uma letra
        if len(try_letra) != 1:
            print("Digite apenas UMA letra.")
            continue

    except:
        print("Erro ao digitar.")
        continue

    num_try += 1

    # verifica se a letra existe na palavra
    if try_letra in secret_word:
        letras_acertadas += try_letra

    palavra_formada = ""

    for letra_secreta in secret_word:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"

    print("Palavra formada:", palavra_formada)

    # condição de vitória
    if palavra_formada == secret_word:
        os.system("clear")  # Linux/Mac
        # os.system("cls")  # Windows

        print("VOCÊ GANHOU!! PARABÉNS!")
        print("A palavra era:", secret_word)
        print("Tentativas:", num_try)

        break
    


    
