#Curso  Básico de Python
#Nome do Desenvolvedor: Dailton Fernandes
#Versão: 1.0
#Exercício de Lógica de Programação: Linguagem de Programação Python
#Exercício: leitura de três valores e organiza os valores em ordem crescente.

valorA = int(input("Digite o valor A: "))
valorB = int(input("Digite o valor B: "))
valorC = int(input("Digite o valor C: "))

minimo = min(valorA, valorB, valorC)
maximo = max(valorA, valorB, valorC)
meio = (valorA + valorB + valorC) - minimo - maximo


print("Os valores em ordem crescente são: ", minimo, meio, maximo)