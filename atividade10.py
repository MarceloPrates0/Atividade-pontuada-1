import os
os.system ("clear")

combustivel = input("""
Combustíveis disponíveis, insira abaixo qual deseja:
A \t G
Álcool \t Gasolina
R$3,79 \t R$6,59                                                            
""").upper()

litros = float(input("Quanto litros irá querer?: "))

match combustivel:
    case "A":
        combustivel_valor = 3.79
        if litros < 25:
            desconto = combustivel_valor - (combustivel_valor * 0.02)
            total = desconto * litros
            print(f"Seu valor total a pagar será R${total:.2f}")
        else:
            desconto = combustivel_valor - (combustivel_valor * 0.04)
            total = desconto * litros
            print(f"Seu valor total a pagar será R${total:.2f}")
    case "G":
        combustivel_valor = 6.59
        if litros < 25:
            desconto = combustivel_valor - (combustivel_valor * 0.03)
            total = desconto * litros
            print(f"Seu valor total a pagar será R${total:.2f}")
        else:
            desconto = combustivel_valor - (combustivel_valor * 0.05)
            total = desconto * litros
            print(f"Seu valor total a pagar será R${total:.2f}")

       

