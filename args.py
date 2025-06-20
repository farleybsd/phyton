"""
1. Em Python, *args é usado em uma função para aceitar um número variável de argumentos
   posicionais — ou seja, você pode passar vários valores sem precisar declarar todos
   eles como parâmetros formais.

2. Quando usar:
        * Quando você não sabe quantos argumentos serão passados para a função.
        * Para funções mais flexíveis, como somadores, acumuladores, etc.
"""
def somar(*args) -> int:
    """
    :param args:
    :return:
    """
    return sum(args)

print(somar(1, 2, 3))       # 6
print(somar(10, 20, 30, 40))  # 100