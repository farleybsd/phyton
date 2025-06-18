"""
Recebendo dados do Usuario
"""
# Entrada De Dados
nome = input("Qual o Seu Nome ?") # Input Entrada
print(f'Seja Bem-Vindo(a) {nome}')

idade = input("Qual a sua idade ?")

print(f'A {nome} tem {idade} anos')


print(f'A {nome} nasceu em, {2025 - int(idade)}')