nome = input('Digite seu nome: ')
print ("Seja bem vindo caro aluno(a):", nome)
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
media = (nota1+nota2)/2
if media < 7:
    print ('Reprovado')
elif media == 10:
    print( 'Aprovado com excelencia')
else:
    print("Aprovado")