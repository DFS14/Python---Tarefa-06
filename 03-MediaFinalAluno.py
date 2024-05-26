#Curso  Básico de Python
#Nome do Desenvolvedor: Dailton Fernandes
#Versão: 1.0
#Exercício de Lógica de Programação: Linguagem de Programação Python
#Exercício: Média Final (>= 5) referente a quatro valores

nota1 = int(input("Digite uma nota: "))
nota2 = int(input("Digite uma nota: "))
nota3 = int(input("Digite uma nota: "))
nota4 = int(input("Digite uma nota: "))

media = float(nota1 + nota2 + nota3 + nota4)/4
print("A média final é: ", media)

if media >= 5:
    print("Aprovado")
else:
    print("Reprovado")
    