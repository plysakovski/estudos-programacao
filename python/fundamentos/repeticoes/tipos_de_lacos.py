# Estruturas de Repetição
# contador
for i in range(1, 11):
    print(i)

print("Fim do laço contador")

"""
Repetição pré-condicional (enquanto 0,N)
- O laço é executado enquanto a condição for verdadeira.
"""
# pré-condicional (enquanto 0,N)
i = 0
while i < 10:
    print(i)
    i += 1
print("Fim do laço pré-condicional")

# Ou

soma = 0
while True:
    n = float(input("Digite um número (0 para sair): "))
    soma += n
    if n == 0:
        break

print(f"A soma dos números é: {soma}")
# pós-condicional (repita 1,N)
