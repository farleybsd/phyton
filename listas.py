"""
Listas
Listas em python funciona como vetores/matrizes (arrays) em outras linguagens, com a diferenca
de serem dinamico e tambem de podermos colocar QUALQUER tipo de dado.

Linguagem como C/Java: arrays
    - Possuem tamanho e tipo de dado Fixo;
    Ou seja, nestas lingugens se voce criar um array do tipo int e como tamanho 5, este array
    sera SEMPRE do tipo inteiro e poderar ter sempre no maximo 5 valores.

ja em python :
- Dinamico: Nao possuem tamanho fixo ou seja  podemos criar a lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dado: Nao possuem tipo de dado fixpo ou seja podemos colocar qualquer tipo de dado;

As lista em python sao repesentadas por COLCHETES: []
"""
lista1 = [1,99,4,15,22,3,1,44,42,27]
lista2 = ['F','A','R','L','E','Y']
list4 = list(range(11))
if 8 in list4:
    print("Encontrei numero 8")
else :
    print("Nao Encontrei numero 8")

# Definindo a classe Usuario
class Usuario:
    def __init__(self,nome: str,email: str):
        self.nome = nome
        self.email = email

    def exibir(self) -> None:
        print(f"Nome: {self.nome}, email: {self.email}")


# Criando uma lista vazia de usuários
usuarios: list[Usuario] = []

# Criando instâncias de Usuario e adicionando à lista
usuario1 : Usuario = Usuario("Ana", "ana@email.com")
usuario2 : Usuario = Usuario("Bruno", "bruno@email.com")

usuarios.append(usuario1)
usuarios.append(usuario2)

# Exibindo os dados dos usuários na lista
for u in usuarios:
    u.exibir()

for email in usuarios:
    print(f"Email: {email.email}")
