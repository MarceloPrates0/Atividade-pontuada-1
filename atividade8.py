import os
os.system ("clear")

cor = input("Insira a cor do CD de seu interesse: ").lower()

match cor:
    case "verde":
        print("O preço dos CD's verdes estão R$10/unidade")
    case "azul":
        print("O preço dos CD's azuis estão R$20/unidade")
    case "amarelo":
        print("O preço dos CD's amarelos estão R$30/unidade")
    case "vermelho":
        print("O preço dos CD's vermelhos estão R$40/unidade")