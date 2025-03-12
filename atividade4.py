import os
os.system ("clear")

print("""
Morango \t Maçã
R$2,50 o kg \t R$1,80 o kg          
""")

fruta = int(input("""
Você irá querer qual fruta? Insira abaixo
1 \t \t 2
Morango \t Maçã
"""))

match fruta:
    case 1:
        quilos = float(input("Quantos quilos irá querer?: "))
        if quilos < 5:
            valor_quilo = 2.50
        else:
            valor_quilo = 2.20
        valor_total = valor_quilo*quilos
        if valor_total >= 15 or quilos >= 10:
            valor_total_desconto = valor_total-(valor_total * 0.10)
        print(f"Ficará no total R${valor_total:.2f}")
    case 2:
        quilos = float(input("Quantos quilos irá querer?: "))
        if quilos < 5:
            valor_quilo = 1.80
        else:
            valor_quilo = 1.50
        valor_total = valor_quilo*quilos
        if valor_total >= 15 or quilos >= 10:
            valor_total_desconto = valor_total-(valor_total * 0.10)
        print(f"Ficará no total R${valor_total:.2f}")
    case _:
        print("Fruta inválida")