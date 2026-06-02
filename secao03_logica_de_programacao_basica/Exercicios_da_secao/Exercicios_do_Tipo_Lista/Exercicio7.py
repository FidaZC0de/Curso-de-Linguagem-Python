# Dada a lista [1, 3, 2, 1, 4, 3, 1, 2, 5, 1], conte quantas vezes
# cada número aparece e exiba o resultado — sem usar .count().

lista = [1, 3, 2, 1, 4, 3, 1, 2, 5, 1] #Crie a lista com os numeros repetidos

for numero in lista: #Criei o primeiro for para percorrer a lista 
   contador_de_vezes = 0 #Criei uma variável para armazenar a quantidade de vezes que um numero apareceu 
   for outro_numero in lista: #Fiz outro loop for para a criação de um numero que eu pudesse comparar com o numero já existente
    if numero == outro_numero: # fiz um if para comparar um numero com um outro numero e ver se eles são iguais 
     contador_de_vezes += 1  #  adicionei a incrementação para cada vez que um numero igual à outro
   print(f"O numero {numero} apareceu {contador_de_vezes} vez(es)") # Fiz a impressão final 




