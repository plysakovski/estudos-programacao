# Resolvendo um problema com todos os laços
# Exemplo: Dados 10 médias pelo usuário, contar quantos foram aprovados e quantos foram reprovados.

aprov = 0
reprov = 0
voltas = 1

while True:
    media = float(input("Digite uma média: "))
    if media >= 6:
        aprov = aprov + 1
    else:
        reprov = reprov + 1

    voltas = voltas + 1
    if voltas > 10:
        break

print(f"Aprovados: {aprov}\nReprovados: {reprov}")

aprov2 = 0
reprov2 = 0
for voltas in range(1, 11, 1):
    media = float(input("Digite uma média: "))
    if media >= 6:
        aprov2 = aprov2 + 1
    else:
        reprov2 = reprov2 + 1

print(f"Aprovados: {aprov}\nReprovados: {reprov}")
