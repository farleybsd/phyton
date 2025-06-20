"""
Tuplas  sao bastante parecidas com listas
existem basicamente duas diferencas
    1. as tuplas sao representadas por parenteses ()
    2. as tuplas sao imutaveis  isso sigfinica que quando criar uma tupla ela nao muda
"""
from typing import Tuple

#  Tupla com múltiplos elementos

pessoa : str = ("Ana",25,"Engenharia")

#Tupla com um único elemento (atenção à vírgula!)
nome : str = ("Ana");


class Usuario:

    def __init__(self, nome : str, email : str):
        self.nome = nome
        self.email = email

    def exibir(self) -> None:
        print(f"Nome: {self.nome}, Email: {self.email}")


#  Exemplo com iteração
usuarios: Tuple[Usuario, Usuario] = (
    Usuario("Ana", "ana@email.com"),
    Usuario("Bruno", "bruno@email.com")
)

# Iteração sobre a tupla
for usuario in usuarios:
    usuario.exibir()

# Acesso direto por índice
print(usuarios[0].nome)   # Ana
print(usuarios[1].email)  # bruno@email.com
