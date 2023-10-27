fruits = ['Apple', 'Banana', 'Orange', 'Lemon']

print('\nUsando For: ')
for fruit in fruits:
    print(fruit, end=" ")


print('\n\nUsando While: ')
cont = 0
while cont < len(fruits):
    print(fruits[cont], end=" ")
    cont += 1

print()
