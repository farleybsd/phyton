"""
Explicação rápida:

try: tenta executar o código que pode gerar erro.
except: trata os erros específicos.
else: executa apenas se não ocorrer nenhum erro.
finally: executa sempre, com ou sem erro (bom para fechar arquivos, conexões, etc).
"""

try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except ValueError:
    print("Erro: entrada inválida. Digite um número inteiro.")
except ZeroDivisionError:
    print("Erro: divisão por zero não é permitida.")
else:
    print(f"Resultado da divisão: {resultado}")
finally:
    print("Operação finalizada.")

