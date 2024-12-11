"""
Faça um programa que pergunte a hora ao
usuário e, baseando-se no horário descrito,
exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17, Boa noite 18-23
"""
horario = input('Olá, qual seu horário? ')

try:
    
   hora = int(horario)

   if hora >= 0 and hora <= 11:
       print('Bom dia')
   elif hora >= 12 and hora <= 17:
       print('Boa tarde') 
   elif hora >= 18 and hora <= 23:
       print('Boa noite') 
   else:
       print('Não reconheço esse horário.')         
except:    
   print('Seu horário estar incorreto')