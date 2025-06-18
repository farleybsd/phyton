"""
Escopo de Variaveis
1. Global
2. Locais
"""
numero: int = 42 # Exemplo de variavel Global

numero2: int = 47

if numero > 10:
    novo = numero + 10 # Exemplo de variavel Local
    print(novo)
