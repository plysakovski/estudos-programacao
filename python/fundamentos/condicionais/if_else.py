# Sintaxe de condicionais em Python
# Estrutura condicional IF
# if True:
#     print("A condição é verdadeira")
# else:
#     print("A condição é falsa")

# # ou em uma linha
# print("A condição é verdadeira") if True else print("A condição é falsa")

# mas todo if tem que possuir uma condição
# - if <condição>: -

# usuário digita um número
num = int(input("Digite um número:"))
# verifica se o número é positivo, negativo ou zero
if num > 0:
    print(f"O número {num} é positivo")
elif num < 0:
    print(f"O número {num} é negativo")
else:
    print(f"O número {num} é zero")

# verifica se o número é par ou ímpar
if num % 2 == 0:
    print(f"O número {num} é par")
else:
    print(f"O número {num} é ímpar")

#  transforma o número negativo em positivo
if num < 0:
    num = -num
    print(f"O número {num} agora é positivo")
