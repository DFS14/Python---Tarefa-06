
#Curso  Básico de Python
#Nome do Desenvolvedor: Dailton Fernandes
#Versão: 1.0
#Exercício de Lógica de Programação: Linguagem de Programação Python
#Exercício: Mensagem de saudação: "Ilmo Sr.(masculino)"/"Ilma Sra."(feminino)

nome = input("Digite o nome: ")
sexo = input("Digite o sexo (M para masculino, F para feminino): ")
if sexo.upper() == 'M':
    print("Ilmo Sr. ", nome)
elif sexo.upper() == 'F':
    print("Ilma Sra. ", nome)
else:
    print("Entrada inválida para o sexo.")
