#BeeCrowd - 1020


# Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

#Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. 
# Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. 
# Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

def calcular_idade_em_anos_meses_dias(idade_dias):
    anos = idade_dias // 365
    resto = idade_dias % 365
    meses = resto // 30
    dias = resto % 30
    return anos, meses, dias

# Exemplo de uso
idade_dias = int(input("Digite a idade em dias: "))  # Entrada de um valor inteiro
anos, meses, dias = calcular_idade_em_anos_meses_dias(idade_dias)
print(f"{anos} ano(s), {meses} mes(es) e {dias} dia(s)")
 