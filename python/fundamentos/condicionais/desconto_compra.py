# Tarefa:
# Fazer um algoritmo que leia a compra de um usário.
# Caso ela seja acima de 300 reias efetuar desco de 10% e
# exibir o valor final da compra, caso contrário exibir o valor da compra sem desconto.
# Exemplos de entrada e saída:
# Entrada: 400  Saída: 360
# Entrada: 150  Saída: 150

# ler a compra do usuário
valor_compra = float(input("Digite o valor da compra:"))
# verificar se o valor da compra é maior que 300
if valor_compra > 300:
    # calcular o valor final da compra com desconto de 10%
    valor_final = valor_compra * 0.9
    #  exibir o valor final da compra com desconto
    print(f"O valor final da compra com desconto é: {valor_final}")
    # caso contrário exibir o valor da compra sem desconto
else:
    # exibir o valor da compra sem desconto
    print(f"O valor da compra sem desconto é: {valor_compra}")
