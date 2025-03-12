import os
os.system ("clear")

renda_mensal = float(input("Insura sua renda mensal: R$"))
emprestimo = float(input("Quanto de empréstimo você deseja?: R$"))

renda_por10 = renda_mensal * 10
if emprestimo > renda_por10:
    print("Não é possível realizar o empréstimo.")
else:
    print("Foi possível realizar o empréstimo.")
    parcelas = int(input("Em quantas parcelas você irá pagar o empréstimo? "))
    valor_parcela = emprestimo / parcelas
    valor_pagamento= renda_mensal * 0.3

    if valor_parcela > valor_pagamento:
        print("Quantidade inválida de parcelas, escolha uma quantidade que represente ao menos 30% de sua renda mensal por parcela.")
    else:
        print(f"\nVocê pagará em {parcelas} parcelas") 
        print(f"Você pagará o total de R${valor_parcela:.2f} por parcela.") 


