print("*********************************")
print("Bem vinde ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Escolha o seu número: ")

print("Você escolheu o número ", chute_str)

chute = int(chute_str)

acertou = chute == numero_secreto
chute_maior = chute > numero_secreto
chute_menor = chute < numero_secreto

if (acertou):
    print("Você acertou o número secreto")
else:
    if (chute_maior):
        print("Erroooou! Você esclheu um número maior que o número secreto :(")
    elif (chute_menor):
        print("Erroooou! Você esclheu um número menor que o número secreto :(")

print("Fim do Jogo!")
