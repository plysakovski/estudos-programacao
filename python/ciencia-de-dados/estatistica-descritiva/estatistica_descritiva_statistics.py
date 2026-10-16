# Importação de bibliotecas
from statistics import mean, median, mode, variance, stdev, quantiles

# Declaração dos meus dados iniciais
vendas = [120, 150, 130, 170, 200, 180, 160, 190, 150]

# Média simples
media = mean(vendas)

# Mediana
mediana = median(vendas)

# Moda
moda = mode(vendas)

# Valor máximo
maximo = max(vendas)

# Valor mínimo
minimo = min(vendas)

# Amplitude
amplitude = maximo - minimo

# Variância
variancia = variance(vendas)

# Desvio padrão
desvio_padrao = stdev(vendas)

# Coeficiente de Variação
cv = desvio_padrao / media * 100

# Quartis, decis e centis
quartis = quantiles(vendas, n=4, method="inclusive")
decis = quantiles(vendas, n=10, method="inclusive")
centis = quantiles(vendas, n=100, method="inclusive")

print("Estatística Descritiva com a biblioteca statistics:")
print(f"Média: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Valor Máximo: {maximo}")
print(f"Valor Mínimo: {minimo}")
print(f"Amplitude: {amplitude}")
print(f"Variância: {variancia}")
print(f"Desvio Padrão: {desvio_padrao}")
print(f"Coeficiente de Variação: {cv}%")
print(f"Quartis: {quartis}")
print(f"Decis: {decis}")
print(f"Centis: {centis}")
