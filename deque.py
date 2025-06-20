"""
Modulo Collections - Deque
Podemos dizer que o deque e uma lista de alta performance
"""

from collections import  deque

#Criando Deques

deq = deque('Farley')
print(deq)

#Adicioando elementos do deque no final
deq.append('y')
print(deq)

#Adicioando no Comeco
deq.appendleft('Tha')

print(deq)