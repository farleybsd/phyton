"""
Em Python, a dorma geral de definir uma funcao e:
def nome_da_funcao(parametro_de_entrada):
    bloco_da_funcao

Onde:
nome_da_funcao -> SEMPRE, com letras minusculas, e se for nome composto separado por underline (snake case)
parametros_de_entrada -> Opcionais, onde tendo mais de um deve ser separdo por virgula podendo ser
opcionais ou nao
"""
# Definindo uma fucao
def diz_oi():
    print('oi')

diz_oi()

"""
Funcoes Com Retorno
"""

# Classe

class Usuario:

    def __init__(self, nome: str, email: str):
        self.nome = nome
        self.email = email

    def exibir(self) -> None:
        print(f"Nome: {self.nome}, Email: {self.email}")

# Função tipada que retorna um objeto Usuario
def criar_Usuario(nome: str, email: str) -> Usuario:
    return Usuario(nome, email)

# Exemplo de uso
novo_usuario: Usuario = criar_Usuario("Ana", "ana@email.com")
novo_usuario.exibir()

def saudacao(nome: str = "Visitante") -> None:
    print(f"Olá, {nome}!")

saudacao("Ana")        # Olá, Ana!
saudacao()             # Olá, Visitante!