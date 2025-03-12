import os
os.system ("clear")

primeiro_numero = int(input("Digite o valor A: "))
segundo_numero = int(input("Digite o valor B: "))
print("\n* = Multiplicação \n+ = Adição \n- = Subtração \n/ = Divisão")
operador = input("Digite a operação que deseja: ")

match operador:
    case "+":
        resultado = primeiro_numero + segundo_numero
    case "-":
        resultado = primeiro_numero - segundo_numero
    case "*":
        resultado = primeiro_numero * segundo_numero
    case "/":
        resultado = primeiro_numero / segundo_numero
    case _:
        resultado = "Operação inválida"

print(f"\nSeu resultado é: {resultado}")