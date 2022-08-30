'''
Faça um Programa que verifique se uma 
letra digitada é vogal ou consoante.
'''

letra = input('Digite uma letra: ').upper()

vogal = letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra =='U'

if(vogal):
    print('Essa letra é vogal')
else:
    print('Essa letra é consoante')

