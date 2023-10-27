# Coleta as informações
name = input('Qual seu nome? ')
age = input('Qual sua idade? ')

# Formas de mostrar na tela

# 1 - Usando F-string
print(f'1 - Usuário: {name}  idade: {age}')

# 2 - Usando str.format()
print('2 - Usuário: {}  idade: {}'.format(name, age))

# 3 - Usando concatenação de strings
print('3 - Usuário: ' + name + '  idade: ' + age)

# 4 - Usando operador de formatação '%' (não recomendado em Python 3)
print('4 - Usuário: %s  idade: %s' % (name, age))

# 5 - Usando templates de strings
import string
template = string.Template('5 - Usuário: $name  idade: $age')
print(template.substitute(name=name, age=age))
