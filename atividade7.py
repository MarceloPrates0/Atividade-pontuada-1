import os
os.system ("clear")

produto = int(input("""
Insira o produto que você quer abaixo:
1 \t \t 2
Produto um \t Produto dois 
R$2,00 \t \t R$3,00                               
"""))

match produto:
    case 1:
        preço = 2
        quantidade = int(input("Insira a quantidade que você deseja: "))
        valor = quantidade * preço
        if quantidade <= 5:
            desconto = valor - (valor * 0.02)
        elif quantidade <= 10:
            desconto = valor - (valor * 0.03)
        else:
            desconto = valor - (valor * 0.05)
        print(f"Você pagará o total de R${desconto:.2f}")
    case 2:
        preço = 3
        quantidade = int(input("Insira a quantidade que você deseja: "))
        valor = quantidade * preço
        if quantidade <= 5:
            desconto = valor - (valor * 0.02)
        elif quantidade <= 10:
            desconto = valor - (valor * 0.03)
        else:
            desconto = valor - (valor * 0.05)
        print(f"Você pagará o total de R${desconto:.2f}")