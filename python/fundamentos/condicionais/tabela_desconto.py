# tarefa:
# criar um algoritimo que receba o valor bruto do pacote,
# a categoria dos assetos em um voo e a quantidade de viajantes

# tabela de desconto:
# categoria Economica: 2 viajante = 3% , 3 viajante = 4% , 4 ou mais viajantes = 5%
# categoria Executiva: 2 viajante = 5% , 3 viajante = 7% , 4 ou mais viajantes = 8%
# categoria Primeira Classe: 2 viajante = 10% , 3 viajante = 15% , 4 ou mais viajantes = 20%

# entrada de dados
valor_bruto = float(input("Digite o valor bruto do pacote: "))
categoria = input(
    "Digite a categoria dos assentos (Economica, Executiva, Primeira Classe): "
)
quantidade_viajantes = int(input("Digite a quantidade de viajantes: "))

# verificar a categoria e aplicar o desconto correspondente
if categoria.lower() == "economica":
    if quantidade_viajantes == 2:
        desconto = 0.03
    elif quantidade_viajantes == 3:
        desconto = 0.04
    elif quantidade_viajantes >= 4:
        desconto = 0.05
    else:
        desconto = 0
elif categoria.lower() == "executiva":
    if quantidade_viajantes == 2:
        desconto = 0.05
    elif quantidade_viajantes == 3:
        desconto = 0.07
    elif quantidade_viajantes >= 4:
        desconto = 0.08
    else:
        desconto = 0
elif categoria.lower() == "primeira classe":
    if quantidade_viajantes == 2:
        desconto = 0.10
    elif quantidade_viajantes == 3:
        desconto = 0.15
    elif quantidade_viajantes >= 4:
        desconto = 0.20
    else:
        desconto = 0

# calcular o valor do desconto e o valor final
valor_desconto = valor_bruto * desconto
valor_final = valor_bruto - valor_desconto

# exibir os resultados
print(f"Valor bruto: R$ {valor_bruto:.2f}")
print(f"Desconto: R$ {valor_desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")
