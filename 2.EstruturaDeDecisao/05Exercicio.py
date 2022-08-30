'''
Faça um programa para a leitura de duas notas 
parciais de um aluno. O programa deve calcular 
a média alcançada por aluno e apresentar:
A mensagem "Aprovado", 
se a média alcançada for  maior ou igual a sete;
A mensagem "Reprovado", 
se a média for menor do que sete;
A mensagem "Aprovado com Distinção", 
se a média for igual a dez.
'''

nota = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota + nota2) / 2

aprovado_com_distincao = media == 10.00
aprovado = media >= 7 and media <= 9.999999999999999

if(aprovado_com_distincao):
    print('Aprovado com Distinção')
elif(aprovado):
    print('Aprovado')
else:
    print('Reprovado')
