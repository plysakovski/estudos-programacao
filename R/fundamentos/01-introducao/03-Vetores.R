# variavel c => é do tipo vetor
idadevetor <- c(37,20,32)
nomeVetor <- c("André","Tiago","Roger")

print(nomeVetor)

vetorNumerico <- c(11,22,33)
vetorNumericoDois <- c(44,55,66)
#Soma de vetores -> v1.pos(0) + v2.pos(0) = vSoma.pos(0)
vetorSoma <- vetorNumerico + vetorNumericoDois
print(vetorSoma)

media <- mean(vetorSoma)


#Aprendendo Matriz Quadrada

#Matriz 2x2
matrizTeste <- matrix(c(11,22,33,44), nrow = 2, ncol = 2)
print(matrizTesteDois)

# Matriz 3x3
matrizTesteDois <- matrix(c(11,22,33,44,55,66,77,88,99), nrow = 3, ncol= 3)
print(matrixTeste)


soma <- sum(matrizTesteDois)
print(soma)
