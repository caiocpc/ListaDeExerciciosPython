'''
Faça um Programa que verifique se uma 
letra digitada é "F" ou "M". Conforme 
a letra escrever: 
F - Feminino, 
M - Masculino, 
Sexo Inválido.
'''

sexo = input('Qual é o seu sexo (F) Feminino ou (M)Masculino: ').upper()
# upper() para que a entrada do usuário seja sempre maiúsculo.
masculino = sexo == 'M'
feminino = sexo == 'F'

if(masculino):
    print('Masculino')
elif(feminino):
    print('Feminino')
else:
    print('Sexo inválido')

