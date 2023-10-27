"""
Esse código mostra como usar um simples controle de decisão
"""

# Coleta as informações do usuário
name = input('Qual seu nome? ')
age = int(input('Qual sua idade? '))

# Controle de decisão
if age >= 18:
    print(f'{name} é maior de idade.')
else:
    print(f'{name} menor de idade.')
