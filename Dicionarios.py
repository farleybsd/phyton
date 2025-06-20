"""
Dicionarios em algumas linguagens de programacao os dicionarios python sao conhecidos como maps
Dicionarios  sao colecoes de tipo chave/valor
Dicionarios sao representados por chaves {}
"""

from typing import Dict

#paises = dict({'br': 'Brasil','eua':'Estados Unidos'})
paises = {'br': 'Brasil','eua':'Estados Unidos'}
receita = {'Jan':100,'Fev':250,'MAR':400}

class Usuario:
    def __init__(self, nome: str, email: str):
        self.nome = nome
        self.email = email

    def exibir(self) -> None:
        print(f"Nome: {self.nome}, Email: {self.email}")

# Dicionário com chave `str` e valor `Usuario`
usuarios: Dict[str, Usuario] = {
    "ana": Usuario("Ana", "ana@email.com"),
    "bruno": Usuario("Bruno", "bruno@email.com")
}

# Acessando e exibindo
usuarios["ana"].exibir()
usuarios["bruno"].exibir()
print(paises.get('br'))


for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

#Chave e valor
for chave in receita:
    print(f'Em {chave} recebi R$: {receita[chave]}')

for chave,valor in receita.items():
    print(f'Chave {chave} Valor: {valor}')

print("Soma:", sum(receita.values()))
print("Máximo:", max(receita.values()))
print("Mínimo:", min(receita.values()))