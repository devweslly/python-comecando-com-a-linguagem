print("*********************************")
print("Bem vinde ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Escolha o seu número: ")

print("Você escolheu o número ", chute_str)

chute = int(chute_str)

if chute == numero_secreto:
    print("Você acertou o número secreto")
else:
    print("Você não acertou o número secreto :(")

print("Fim do Jogo!")
