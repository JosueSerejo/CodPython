# Com base na tabela abaixo, escreva um programa que leia o código de um item 
# e a quantidade deste item. 
# A seguir, calcule e mostre o valor da conta a pagar.

#Entrada
#O arquivo de entrada contém dois valores inteiros 
# correspondentes ao código e à quantidade de um item conforme tabela acima.

#Saída
#O arquivo de saída deve conter a mensagem "Total: R$ " 
# seguido pelo valor a ser pago, com 2 casas após o ponto decimal.

#Code = int(input())
#Quantity = int(input())

#if Code == 1:
  #  print(f'Total: R$: {(Quantity * 4.00):.2f}')
#elif Code == 2:
 #   print(f'Total: R$: {(Quantity * 4.50):.2f}')
#elif Code == 3:
   # print(f'Total: R$: {(Quantity * 5.00):.2f}')
#elif Code == 4:
   # print(f'Total: R$: {(Quantity * 2.00):.2f}')
#else:
 #   print(f'Total: R$: {(Quantity * 1.50):.2f}')


# ---------------------------------------------------------------

tabela_precos = {
    1: 4.00,   # Cachorro Quente
    2: 4.50,   # X-Salada
    3: 5.00,   # X-Bacon
    4: 2.00,   # Torrada Simples
    5: 1.50    # Refrigerante
}

codigo, quantidade = map(int, input().split())

valor_total = tabela_precos.get(codigo, 0) * quantidade

print(f"Total: R$ {valor_total:.2f}")
