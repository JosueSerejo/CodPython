#Listas:

#Armazenar múltiplos elementos: Ideal para manter vários itens de um mesmo tipo ou relacionados, como uma coleção de números, strings ou objetos.
#Acessar elementos pelo índice: Como as listas são ordenadas, é fácil acessar itens específicos com base em sua posição.
#Modificar o conteúdo: Listas em Python são mutáveis, então você pode alterar, adicionar ou remover elementos conforme necessário.
#Ordenar e manipular dados: Listas possuem métodos integrados como .sort(), .append(), .remove(), entre outros, que facilitam o gerenciamento dos elementos.
#Exemplo no Estilo BeeCrowd
#Imagine um problema que peça para você receber uma quantidade de números inteiros, armazená-los, e depois exibir a soma dos números pares e a quantidade de números ímpares.

#Exemplo:

# Lê os números e cria uma lista
numeros = list(map(int, input("Digite três números: ").split()))

# Itera sobre a lista e imprime o quadrado de cada número
for numero in numeros:
    print(numero ** 2)


# -------------------------------------------------------------------------------------------------------------------------------------------
