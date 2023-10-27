"""
Código mostra exemplos de laços de repetição
"""

fruits = ['Apple', 'Banana', 'Orange', 'Lemon']

print('\nUsando For: ')
for fruit in fruits:
    print(fruit, end=" ")

print('\n\nUsando While: ')
CONT = 0

while CONT < len(fruits):
    print(fruits[CONT], end=" ")
    CONT += 1

print()
