# Laço contador para - FOR
# Exemplo: Exibir a tabuada de um número dado pelo usuário

tab = int(input("Digite a Tabuada:"))
for volta in range(1, 11, 1):
    mult = tab * volta
    print(f"{tab} x {volta} = {mult}")
