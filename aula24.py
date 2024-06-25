# Operadores in (significa - entre) e 
# not in (significa - não entre)
# Strings são iteráveis
# 0 1 2 3 4 5 
# o t á v i o 
# -6-5-4-3-2-1
#nome = 'Otávio'
# print(nome[2])
# print(nome[2])
# print(nome[-3])
# print('á' in nome)
# print('z' in nome)
# print(10 * '-')
# print('vio' not in nome)
# print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome} ') 

#variavel_a = 1 or 0
#variavel_b = 0 or 1
#print(variavel_a, variavel_a)
numero = 10
 
if numero > 1:
    if numero > 2:
        if numero > 3:
            print('Número maior que 3')
        else:
            print('Número menor que 3')
    else:
        print('Número menor que 2')
else:
    print('Número menor que 1')