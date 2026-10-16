import numpy as np

# obtenção da estatística descritiva com numpy
vendas = np.array([120, 150, 130, 170, 200, 180, 160, 190, 150])

valores, frequencias = np.unique(vendas, return_counts=True)

media = vendas.mean()
mediana = np.median(vendas)
moda = valores[frequencias.argmax()]

maximo = vendas.max()
minimo = vendas.min()
amplitude = np.ptp(vendas)

variancia = vendas.var(ddof=1)
desvio_padrao = vendas.std(ddof=1)
cv = desvio_padrao / media * 100

quartis = np.quantile(vendas, [0.25, 0.50, 0.75])
decis = np.quantile(vendas, np.arange(0.1, 1, 0.1))
centis = np.quantile(vendas, np.arange(0.01, 1, 0.01))


# obtenção da estatística descritiva com pandas/dataframes
import pandas as pd

df = pd.DataFrame({
    "vendas": [120, 150, 130, 170, 200, 180, 160, 190, 150]
})

vendas = df["vendas"]

media = vendas.mean()
mediana = vendas.median()
moda = vendas.mode().iloc[0]

maximo = vendas.max()
minimo = vendas.min()
amplitude = maximo - minimo

variancia = vendas.var()
desvio_padrao = vendas.std()
cv = desvio_padrao / media * 100

quartis = vendas.quantile([0.25, 0.50, 0.75])
decis = vendas.quantile([i / 10 for i in range(1, 10)])
centis = vendas.quantile([i / 100 for i in range(1, 100)])

print("Estatística Descritiva com NumPy:")
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
