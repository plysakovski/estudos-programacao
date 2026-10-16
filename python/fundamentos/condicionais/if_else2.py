# Tarefa:
# criar um algoritmo que leia dois numeros e exiba o maior deles.
# num1 = float(input("Digite o primeiro número: "))
# num2 = float(input("Digite o segundo número: "))

# if num1 > num2:
#     print(f"O maior número é: {num1}")
# else:
#     print(f"O maior número é: {num2}")


# Tarefa 2:
# criar um algoritmo que leia quatro números e exiba o maior deles.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
num4 = float(input("Digite o quarto número: "))

if num1 >= num2 and num1 >= num3 and num1 >= num4:
    print(f"O maior número é: {num1}")
elif num2 >= num3 and num2 >= num4:
    print(f"O maior número é: {num2}")
elif num3 >= num4:
    print(f"O maior número é: {num3}")
else:
    print(f"O maior número é: {num4}")
