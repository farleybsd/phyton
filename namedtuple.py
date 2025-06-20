"""
Modulo Collections - Named Tuple
Sao tuplas diferenciadas,onde,espeficamos um nome para a mesma e tambem parametros
"""

from collections import namedtuple
# Precisamos definir o nome e parametro

# Forma 1 - Declaracao Named Tuple
cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaracao Named Tuple
cachorro = namedtuple('cachorro', 'idade raca nome')


# Forma 3 - Declaracao Named Tuple
Cachorro = namedtuple('Cachorro', ['idade', 'raca', 'nome'])

# usando
ray = Cachorro(idade=2, raca='Chow-Chow', nome='Ray')
print(ray)
print(ray)              # Cachorro(idade=2, raca='Chow-Chow', nome='Ray')
print(ray.nome)         # Ray
print(ray[1])           # Chow-Chow
