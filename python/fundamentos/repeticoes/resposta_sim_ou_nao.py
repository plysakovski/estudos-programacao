resp = input("Digite '[S]im' ou '[N]ão': ").strip().lower()
while resp != "s" and resp != "n":
    print("Resposta inválida. Digite '[S]im' ou '[N]ão'.")
    resp = input()
print(f"Você digitou a letra válida: {resp}")
