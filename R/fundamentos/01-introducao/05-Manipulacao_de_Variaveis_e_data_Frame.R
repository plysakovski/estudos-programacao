nome <- 'Pedro'
nomeDois = 'Carol'

#Mostrar Resultados
print(nome)
print(nomeDois)

#Criação do data Frame
dataFrame <- data.frame(nome= c('Pedro', 'Carol'), idade = c(20,27))
print(dataFrame)

#Renomear Colunas
colnames(dataFrame)[colnames(dataFrame) == 'idade'] <- 'Idade'
print(dataFrame)
colnames(dataFrame)[colnames(dataFrame) =='nome'] <- "Nome"
print(dataFrame)

#Manipulação de variáveis

testeIdadeFrame <- dataFrame$Idade
print(testeIdadeFrame)

#Selecionar valores de uma coluna utilizando $
colunaSelecionada <- dataFrame$Nome
print(colunaSelecionada)

#Selecionar valor de uma coluna utilizando outra maneira
colunaSelecionadaDois <- dataFrame[,c('Nome')]

print(colunaSelecionadaDois)


# data frame de exemplo
data_frame <- data.frame(
  nome = c("Alice", "Bob", "Charlie"),
  idade = c(30,25,35),
  cidade = c("Nova York", "Los Angeles", "Chicago")
)
print(data_frame)

#Selecionar duas ou mais colunas:
duasColunasSelecionadas <- data_frame[, c("nome", "cidade")]
print(duasColunasSelecionadas)
