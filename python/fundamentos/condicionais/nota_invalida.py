# Ler a nota
nota = float(input("Digite a nota: "))
# Se a nota for maior do que 10
if nota > 10:
    print("Nota inválida")
# Se a nota for menor do que 0
elif nota < 0:
    print("Nota inválida")
# se não for maior do que 10 e nem menor do que 0, então a nota é válida
else:
    print("Nota válida")
