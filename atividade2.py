import os
os.system ("clear")

nome = input("Insira seu nome: ")
genero = input("""
Insira o gênero ao qual você se identifica abaixo: 
F \t\t M
Feminino \t Masculino
""")
estado_civil = int(input("""
Insira seu estado civil atual abaixo:
1 - Solteiro
2 - Casado
3 - Viúvo
4 - Divorciado
5 - Separado judicialmente
                                                                                                          
"""))
match estado_civil:
    case 2:
        tempo = input("Está a quanto tempo casado? Especifique se são anos/meses: ")

print(f"\nSeu nome: {nome}")

match genero:
    case "M" | "m":
        print(f"Seu genero: Masculino")
    case "f" | "F":
        print(f"Seu genero: Feminino")
        
print(f"Seu estado civil é {estado_civil}")

if estado_civil == 2:
    print(f"Você está casado(a) a {tempo}")




