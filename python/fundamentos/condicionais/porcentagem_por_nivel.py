# Tarefa:
# Crie um algoritmo que receba o tipo de assinatura do cliente, o faturamento anual dele
# e que calcule e exiba qual o valor do bônus que o cliente deve pagar a vocês. Seguindo a tabela abaixo:
# basic = 30% do faturamento anual
# silver = 20% do faturamento anual
# gold = 10% do faturamento anual
# platinum = 5% do faturamento anual

# entrada de dados
tipo_assinatura = input(
    "Digite o tipo de assinatura do cliente (basic, silver, gold, platinum): "
)
faturamento_anual = float(input("Digite o faturamento anual do cliente: "))

# cálculo do bônus
if tipo_assinatura.lower() == "basic":
    bonus = faturamento_anual * 0.3
elif tipo_assinatura.lower() == "silver":
    bonus = faturamento_anual * 0.2
elif tipo_assinatura.lower() == "gold":
    bonus = faturamento_anual * 0.1
elif tipo_assinatura.lower() == "platinum":
    bonus = faturamento_anual * 0.05
else:
    print("Tipo de assinatura inválido.")
    bonus = 0

# exibição do resultado
print(f"O valor do bônus que o cliente deve pagar é: R$ {bonus:.2f}")
