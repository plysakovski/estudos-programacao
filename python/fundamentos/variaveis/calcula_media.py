# Ler o primeiro valor
nota1 = float(input("Digite a primeira nota:"))
# Ler o segundo valor
nota2 = float(input("Digite a segunda nota:"))
# Ler o terceiro valor
nota3 = float(input("Digite a terceira nota:"))
# mostra os tipos de dados das variáveis
print(
    f"Tipo da nota 1 = {type(nota1)}\nTipo da nota 2 = {type(nota2)}\nTipo da nota 3 = {type(nota3)}"
)
# Calcular a média
media = (nota1 + nota2 + nota3) / 3
# Exibir a média
print(f"A média das notas é: {media:.2f}")
