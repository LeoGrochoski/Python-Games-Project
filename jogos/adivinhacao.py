print(36*"*")
print("  Bem vindo no jogo de adivinhação! ")
print(36*"*")

numero_secreto = 43

# 1 - Codigo simples de IF referente a comparação de variaveis, jogo de advinhação
# IF -> Serve para testar uma condição e executar um bloco uma única vez.

# if(numero_secreto == chute):
#     print("Você digitou", chute, "Parabéns! Você Acertou!")
# else:
#     print("Você digitou", chute, "Que pena! Você Errou! Tente novamente")


# 2 - Codigo um pouco mais complexo com IF e ELIF referente a comparação de variaveis, jogo de advinhação

# chute_str = input("Digite o seu numer: ")
#
# print("Você digitou", chute_str)
# chute = int(chute_str)
#
# acertou = chute == numero_secreto
# maior = chute > numero_secreto
# menor = chute < numero_secreto
#
# if(acertou):
#     print("Você acertou!")
# else:
#     if(maior):
#         print("Você errou, seu chute foi maior que o numero secreto")
#     elif(menor):
#         print("Você errou, seu chute foi menor que o numero secreto")


# 3 - Codigo completo com WHILE, IF e ELIF, com 3 tentativas de resposta e dica de maior ou menor
# IF e WHILE -> Ambos possuem uma condição de entrada.
# WHILE -> Serve para testar uma condição e executar um bloco enquanto a condição for verdadeira.
# PYTHON não não tem uma estrutura condicional como a do-while

tentativa = 0
rodada = 1
total_rodada = 3

while tentativa <= 2:
    print(f"Tentativa {rodada} de {total_rodada}")
    chute_str = input("Digite o seu numero: ")
    chute = int(chute_str)
    if chute == numero_secreto:
        print("Parabéns! Você acertou.")
        break
    else:
        if chute > numero_secreto:
            print("Errado! O numero secreto é menor que seu chute, tente novamente.")
        elif chute < numero_secreto:
            print("Errado! O numero secreto é maior que seu chute, tente novamente.")
    tentativa = tentativa + 1
    rodada = rodada + 1
if tentativa > 2 and chute != numero_secreto:
    print("Game Over")
