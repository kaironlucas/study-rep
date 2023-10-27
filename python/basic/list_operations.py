"""Esse código mostra simples uso de listas 
"""

frutas = ["maçã", "banana", "laranja"]
print(frutas[0])  # Acessando o primeiro elemento
frutas.append("uva")  # Adicionando uva à lista
frutas.remove("banana")  # Removendo banana da lista

for fruta in frutas:
    print(fruta, end=" ")
