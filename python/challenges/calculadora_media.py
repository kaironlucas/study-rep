"""
Desafio: Programa para calcular a média de números com tratamento de erros.
"""

# Solicita ao usuário que informe a quantidade de números que serão calculados
try:
    n = int(input('De quantos valores deseja calcular a média? '))
except ValueError:
    print("Por favor, insira um valor inteiro válido.")
    exit()

# Variável para armazenar os valores que serão lidos
valores = []

# Loop que adiciona todos os valores digitados pelo usuário
for i in range(n):
    try:
        valor = float(input(f'Digite o valor {i+1}: '))
        valores.append(valor)
    except ValueError:
        print(f"O valor {i+1} não é um número válido. Por favor, insira um número válido.")
        valores.append(0.0)  # Adiciona um valor padrão

# Calcula a média dos valores
if n > 0:
    media = sum(valores) / n
    print(f'Média: {media}')
else:
    print("Não é possível calcular a média com 0 valores.")
