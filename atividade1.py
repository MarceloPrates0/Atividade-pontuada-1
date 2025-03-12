import os
os.system ("clear")

valor_a = int(input("Insira o valor de A: "))
valor_b = int(input("Insira o valor de B: "))
valor_c = int(input("Insira o valor de C: "))

valor_ab = valor_a+valor_b

if valor_ab > valor_c:
    print("A junção dos valores A e B são maiores que a C")
else:
    print("O valor C é maior que a junção dos valores de A e B ")