install.packages("dplyr")
library(dplyr)

#Criar dados
data_frame <- data.frame(
  idade = c(30,25,35,50,15,20),
  genero = c(0,0,1,1,0,1)
)
print(data_frame)

# Filtrar dados: selecionar apenas linhas onde a idade seja maior que 25
dados_filtrados <- data_frame %>% filter(idade > 25)
print(dados_filtrados)

# Agrupar dados por gênero e calcular a média de idade por grupo
dados_agrupados <- data_frame %>%group_by(genero)%>%summarize(media_idade = mean(idade))
print(dados_agrupados)
