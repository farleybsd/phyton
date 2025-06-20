"""
Conjuntos, em qualquer linguagem de programação, fazem referência à teoria dos conjuntos da matemática.

- Em Python, os conjuntos são chamados de sets.

Assim como na matemática:

- Sets (conjuntos) não permitem valores duplicados.
- Sets não mantêm uma ordem específica dos elementos.
- Os elementos não são acessados por índice, ou seja, conjuntos não são indexados.

Conjuntos são ideais para armazenar elementos quando:
- A ordem dos itens não é importante.
- Não há necessidade de trabalhar com chaves ou valores duplicados.

Em Python, os conjuntos (sets) são representados com chaves: `{}`.

Diferença entre conjunto (set) e dicionário (dict) em Python:
- Um **dicionário** armazena **pares chave-valor**.
- Um **conjunto** armazena apenas **valores únicos**.
"""



conjunto = set({1,2,3,4,5,67,2,3})
print(conjunto)  # {1, 2, 3, 4, 5}
frutas = ['banana','pera']

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # União: {1, 2, 3, 4, 5}
print(a & b)  # Interseção: {3}
print(a - b)  # Diferença: {1, 2}
print(a ^ b)  # Diferença simétrica: {1, 2, 4, 5}

c = {1, 2}
c.add(3)         # Adiciona o 3
c.remove(2)      # Remove o 2
c.discard(99)    # Descarta (sem erro, mesmo se não existir)
print(c)         # {1, 3}


if "banana" in frutas:
    print("Tem banana!")
