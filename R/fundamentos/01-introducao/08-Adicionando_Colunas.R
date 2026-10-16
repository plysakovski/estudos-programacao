install.packages("dplyr")
library(dplyr)

# Data frame com valores ausentes
vendas_loja <- data.frame(
  data_venda =  c("2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05"),
  produto = c("A","B", "A", NA, "C"),
  quantidade = c(10,15,20,20,25),
  receita = c(100,150,200,200,250)
)
print(vendas_loja)

# Identifique e conte os valores ausentes em cada coluna
valores_ausentes <- colSums(is.na(vendas_loja))
print(valores_ausentes)

# 1. Calcule a média da quantidade vendida
 media_quantidade <- vendas_loja %>% summarize(media_quantidade = mean(quantidade, na.rm = TRUE))
 print(media_quantidade)

 # 2. Crie uma nova coluna chamada "valor_total" multiplicando a quantidade pela receita
 vendas_com_valor_total <- vendas_loja %>% mutate(valor_total = quantidade * receita)

print(vendas_com_valor_total) 

# 3. Selecione apenas as colunas "data_venda" e "produto"
colunas_selecionadas <- vendas_loja %>% select(data_venda, produto)
print(colunas_selecionadas)
