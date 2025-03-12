import os
os.system ("clear")

nota_um = int(input("Insira sua primeira nota: "))
nota_dois = int(input("Insira sua segunda nota: "))

media = (nota_um + nota_dois) / 2

print(f"Sua média é de {media}")

if media < 4:
    print("Você está reprovado.")
elif media < 6:
    print("Você está de recuperação.")
else:
    print("Você está aprovado.")

