# 01 — Primeiros passos com R

# O console funciona como uma calculadora.
2 + 2
10 / 2
2 ^ 3

# Criando objetos.
nome <- "Estudante FIAP"
idade <- 25
estudando_r <- TRUE

# Exibindo valores.
nome
print(idade)
cat("Olá,", nome, "!\n")

# Descobrindo o tipo e a estrutura de um objeto.
class(nome)
class(idade)
str(estudando_r)

# Criando um vetor e calculando um resumo.
notas <- c(8.5, 7.0, 9.5, 10.0)
mean(notas)
summary(notas)
