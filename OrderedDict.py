"""
Ordered Dict ele mamtem a ordem no dicionario conforme a insercao
tem a  certeza que ele vai manter a ordem da insercao
"""
# Em um dicionario a ordem de insercao dos elementos nao sao garantida

#dicionario = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6}

#for chave , valor in dicionario.items():
#    print(f'Chave {chave} valor {valor}')

from collections import OrderedDict

dicionario = OrderedDict({'a':1,'b':2,'c':3,'d':4,'e':5,'f':6})

for chave , valor in dicionario.items():
    print(f'Chave {chave} valor {valor}')