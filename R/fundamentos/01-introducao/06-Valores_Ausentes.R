# Identificação de valores ausentes em um vetor
vetor <- c(1,2,NA,4,5)
valores_ausentes <- is.na(vetor)
print(valores_ausentes)

# Identificação de valores ausentes em um data frame
data_frame <- data.frame(idade = c(25,NA,30,35), salario = c(50000, 55000, NA, 60000))
valores_ausentes_dois <- is.na(data_frame)
print(valores_ausentes_dois)

# Data frame de exemplo
dados <- data.frame( A = c(1,2, NA,4), B = c(NA,2,3,4))
print(dados)
# Remover linhas com valores ausentes
dados_limpos <- na.omit(dados)
print(dados_limpos)


# Data frame de exemplo 2
dadosDois <- data.frame(
  A = c(1,2,NA,4,5),
  B = c(NA,2,3,4,5)
)
print(dadosDois)

dados_limpos_dois <- na.omit(dadosDois)

print(dados_limpos_dois)
