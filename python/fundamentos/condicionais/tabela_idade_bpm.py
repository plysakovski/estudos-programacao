# tarefa:
# Criar um algoritmo que leia a idade e o BPM e exiba se está acima ou abaixo do recomendado para a idade.
# mostrar a quantidade de bpm acima ou abaixo do recomendado para a idade.
idade = int(input("Digite sua idade: "))
bpm = int(input("Digite seu BPM: "))

# idade até 2 anos: 120 a 140 bpm
if idade <= 2 and idade >= 0:
    if bpm < 120 or bpm > 140:
        print("BPM fora do recomendado para a idade.")
        print(
            f"Quantidade de BPM acima do recomendado: {bpm - 140}"
            if bpm > 140
            else f"Quantidade de BPM abaixo do recomendado: {120 - bpm}"
        )
    else:
        print("BPM dentro do recomendado para a idade.")
# idade entre 8 a 17 anos: 80 a 100 bpm
elif idade >= 8 and idade <= 17:
    if bpm < 80 or bpm > 100:
        print("BPM fora do recomendado para a idade.")
        print(
            f"Quantidade de BPM acima do recomendado: {bpm - 100}"
            if bpm > 100
            else f"Quantidade de BPM abaixo do recomendado: {80 - bpm}"
        )
    else:
        print("BPM dentro do recomendado para a idade.")
# idade entre 18 a 65 anos: 70 a 80 bpm
elif idade >= 18 and idade <= 65:
    if bpm < 70 or bpm > 80:
        print("BPM fora do recomendado para a idade.")
        print(
            f"Quantidade de BPM acima do recomendado: {bpm - 80}"
            if bpm > 80
            else f"Quantidade de BPM abaixo do recomendado: {70 - bpm}"
        )
    else:
        print("BPM dentro do recomendado para a idade.")
# idade acima de 65 anos: 50 a 60 bpm
elif idade > 65:
    if bpm < 50 or bpm > 60:
        print("BPM fora do recomendado para a idade.")
        print(
            f"Quantidade de BPM acima do recomendado: {bpm - 60}"
            if bpm > 60
            else f"Quantidade de BPM abaixo do recomendado: {50 - bpm}"
        )
    else:
        print("BPM dentro do recomendado para a idade.")
