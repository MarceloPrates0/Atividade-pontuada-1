import os
os.system ("clear")

valor_a = int(input("Insira o valor de A: "))
valor_b = int(input("Insira o valor de B: "))

if valor_a == valor_b:
    valor_ab = valor_a+valor_b
else:
    valor_ab = valor_b*valor_a

print(f"Seu novo valor C, possui o total de: {valor_ab}")