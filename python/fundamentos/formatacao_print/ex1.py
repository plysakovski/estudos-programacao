# Saida de dados : Interação do sistema com o usuário, ou seja, a saída de dados é a forma como o
# sistema apresenta informações para o usuário.
# Em Python, a função print() é usada para exibir informações na tela.
# A função print() pode receber vários argumentos, que podem ser strings, números, variáveis, expressões, etc.
#  A função print() também pode formatar a saída de dados usando diferentes técnicas, como f-strings, método format(),
#  operadores de formatação (%), etc.
#  A formatação de saída de dados permite controlar a aparência e o alinhamento das informações exibidas na tela.


# Usuário digita um valor
valor = input(
    "Digite um valor:"
)  # o input somente lê dados do tipo string, ou seja, texto. Se o usuário digitar um número, ele será lido como texto.
# mostra o valor digitado e o tipo de dado que foi digitado
print(f"O valor digitado foi: {valor} e o tipo de dado é: {type(valor)}")
# converte o valor digitado para inteiro
valor = int(valor)
# mostra o valor depois da conversão e o tipo de dado que foi convertido
print(f"O valor convertido foi: {valor} e o tipo de dado é: {type(valor)}")
# efetua o cálculo do dobro do valor digitado
resposta = valor * 2
# mostra o resultado do cálculo
print(f"O dobro do valor digitado é: {resposta}")


# valor2 = int(input("Digite outro valor:")) --> Nesse caso podemos formatar o input diretamente na raiz dele
