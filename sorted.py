# Sorted

"""
OBS: Não confunda, apesar do nome, com a função sort() que já estudamos em Listas. O sort() só funciona em listas.

Podemos utilizar o sorted() com qualquer iterável.

Como o próprio nome diz, sorted() serve para ordenar.
"""
usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bobiza", "tweets": [], "cor": "amarelo"},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": [], "cor": "preto", "musica": "rock"}
]

print(usuarios)

# Ordenando por username - Ordem Alfabética
print(sorted(usuarios, key=lambda usuario: usuario["username"]))

# Ordenando pelo número de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))

# Último exemplo
musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock n roll, too young to die", "tocou": 32}
]

# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica["tocou"]))

# Ordena da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica["tocou"], reverse=True))
