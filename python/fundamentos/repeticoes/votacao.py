# Tarefa:
# - Crie um algoritmo em que o usuário possa digitar o voto de cada um dos 5 membros da equipe e,
#     ao final, exiba qual console escolhido e com quantos votos cada um dos consoles recebeu.
# => as opções de consoles são: Playstation, Xbox e Nintendo.

# entrada de votos
votos = []
for i in range(5):
    voto = input(f"Digite o voto do membro {i + 1} (Playstation, Xbox, Nintendo): ")
    votos.append(voto)

# contagem de votos
contagem = {}
for voto in votos:
    contagem[voto] = contagem.get(voto, 0) + 1

# exibição dos resultados
for console, votos_recebidos in contagem.items():
    print(f"{console}: {votos_recebidos} votos")
