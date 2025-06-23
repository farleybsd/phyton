"""
Conhecidas como expressao lambdas, ou simplesmente lambdas sao funcoes se, nome ou seja
funcoes anonimas

# Funcao em Python
def soma (a,b) :
    return a + b
"""

# Expressao Lambda
calc = lambda  x: 3 * x + 1
print(calc(3))

# Podemos ter expressoes lambdas com multiplas entradas
nome_completo = lambda  nome,sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo("Farley", "Rufino"))

# Em funcoes python poddemos ter nehuma ou varias entradas em lambdas tambem
amar = lambda : 'Como nao amar pythom'
print(amar())

uma = lambda x: 3 * x + 1
duas = lambda x,y: (x * y) ** 0.5
tres = lambda x,y,z: (x * y) / z
print(uma(3))
print(duas(3,4))
print(tres(3,4,5))

# Outro exemplo
autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke',
           'Frank Herbert', 'Orson Scott Card', 'Douglas Adams', 'H. G. Wells',
           'Leigh Brackett']

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)

def geradora_funcao_quadratica(a, b, c):
    """Retorna a função f(x) = a * x**2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratica(2, 3, -0.5)

print(teste(0))
print(teste(1))
print(teste(2))
print(geradora_funcao_quadratica(3,0,1)(2))