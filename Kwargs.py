"""
permite que você passe argumentos nomeados variáveis (ou seja, pares chave=valor)
para uma função. Ele empacota esses argumentos em um dicionário.
"""

def mostrar_dados(**Kwargs) -> None:
    """
    :param Kwargs:
    :return:
    """
    for chave,valor in Kwargs.items():
        print(f'{chave} = {valor}')

mostrar_dados(nome="Alice", idade=30, cidade="São Paulo")