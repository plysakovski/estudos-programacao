valor1 = 456
valor2 = 3423
valor3 = 2

# Formatação de valores com casas decimais usando o método format em sua forma mais simples
print(
    "Valor 1 = {v1:10.2f}\nValor 2 = {v2:10.2f}\nValor 3 = {v3:10.2f}".format(
        v1=valor1, v2=valor2, v3=valor3
    )
)

# Transforma o valor em inteiro e preenche com 0 a esquerda em um tamanho de 5 caracteres (5 Bits)
print(f"Valor 1 = {valor1:05d}\nValor 2 = {valor2:05d}\nValor 3 = {valor3:05d}")

# %o - > Transforma o valor em octal
print(f"Valor 1 = %o\nValor 2 = %o\nValor 3 = %o" % (valor1, valor2, valor3))
