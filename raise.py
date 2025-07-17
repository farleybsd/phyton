"""
Levantando os próprios erros com raise

raise -> Lança exceções

OBS: O raise não é uma função. É uma palavra reservada, assim como def ou qualquer outra em Python.

Para simplificar, pense no raise como sendo útil para que possamos criar nossas próprias exceções e mensagens de erro.

A forma geral de utilização é:

raise TipoDoErro('Mensagem de erro')
raise  ValueError("ValorIncorreto")
"""
# Exemplo 1

def color(texto,cor):
    cores = ('verde','amarelo','azul','branco')
    if type(texto) is not str:
        raise TypeError('Texto deve ser string')
    if type(cor) is not str:
        raise TypeError('Cor deve ser string')
    if cor not in cores:
        raise ValueError(f'Cor deve ser de tipo de {cores}')
    print(f'O texto {texto} sera impreso na cor {cor}')
    
color("Farley","Azul")
color("Farley","rosa")