"""
Modulo Collections - Counter
Recebe um parametro e retornar um valor com a quantidade de ocorrencia desse elemento
"""
from collections import Counter

lista = [1,1,1,2,2,2,3,3,3 ,4,4]

res = Counter(lista)

print(type(res))
print(res)