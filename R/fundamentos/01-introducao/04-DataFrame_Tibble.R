#
DataFrameTesteUm <- data.frame(nome = c("Rafael", "Karina", "Thiago"),idade = c(37,35,21),
                               casado = c(TRUE, TRUE, FALSE))

print(DataFrameTesteUm)

DataFrameTesteDois <- data.frame(nome = c("Rafael", "Karina", "Thiago", "Camila"),idade = c(37,35,21,23),
         casado = c(TRUE, TRUE, FALSE, FALSE))

print(DataFrameTesteDois)



#Aprendendo Tibble

# Mostra o tipo de dado
tibbleTesteUm <- tibble(nome = c("Pedro", "Carol", "Geraldo"), idade = c(20, 27, 60), endereco = c("Rua x", "Avenida w", "Rua C"))
print(tibbleTesteUm)

# Mostra somente os dados
FrameTesteUm <- data.frame(nome = c("Pedro", "Carol", "Geraldo"), idade = c(20, 27, 60), endereco = c("Rua x","Avenida w","Rua C"))
print(FrameTesteUm)

testeNome <- tibbleTesteUm$nome
print(testeNome)
testeIdade <- tibbleTesteUm$idade
print(testeIdade)
testeEndereco <- tibbleTesteUm$endereco
print(testeEndereco)
