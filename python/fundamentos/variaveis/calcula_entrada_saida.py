# A terminologia: Entrada e Saída (Input e Output) é utilizada para se referir a entrada de dados no programa e a saída de dados do programa.
# Tarefas neste exercicio:
# - construir o algoritmo
# - efetuar os testes com todas as possibilidades
# - mostrar quantas Entradas e saídas de dados teremos no algoritmo

# Dados 3 valores pelo usuário que representa os valores de A, B e C, calcule o Delta
# Entrada: 1 2 3   Saída: -8
# Entrada: -1 2 3  Saída: 16


# ler o valor de A
a = float(input("Digite o valor de A:"))
# ler o valor de B
b = float(input("Digite o valor de B:"))
# ler o valor de C
c = float(input("Digite o valor de C:"))
# calcular o delta
delta = (b**2) - (4 * a * c)
# exibir o resultado
print(f"O valor do delta é: {delta}")
