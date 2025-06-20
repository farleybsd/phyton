"""
Usando list como default_factory, se for fácil agrupar a sequencia dos pares chave-valores num dicionário de listas
"""
from collections import Counter, defaultdict

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

resultado =sorted(d.items())
print(resultado)