# Operadores lógicos
a = True
b = False
c = a and b  # False
d = a or b  # True
e = not a  # False
# and = operador lógico "E" (retorna True se ambos os operandos forem True)
# or = operador lógico "OU" (retorna True se pelo menos um dos operandos for True)
# not = operador lógico "NÃO" (inverte o valor do operando, se for True retorna False e vice-versa)


# Exemplo de uso dos operadores lógicos
idade = int(input("Digite sua idade: "))
# - AND
if idade >= 18 and idade <= 65:
    print("Você é um adulto.")
else:
    print("Você não é um adulto.")

# - OR
if idade < 18 or idade > 65:
    print("Você não é um adulto.")
else:
    print("Você é um adulto.")
# - NOT
if not (idade >= 18 and idade <= 65):
    print("Você não é um adulto.")
else:
    print("Você é um adulto.")

# Agora um exemplo de uso dos operadores lógicos em conjunto com os operadores de comparação
# -AND/NOT/OR
if idade != 0 and not (idade < 18 or idade > 65):
    print("Você é um adulto.")
