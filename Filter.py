"""
Filter server para filtrar dados de uma determinada colecao
"""
import  statistics
valores  = 1,2,3,4,5,6
media = (sum(valores) / len(valores))
print(media)

# dados de um senor
dados = [1.3,2.7,0.8,4.1,4.3,-0.1]
statistica = statistics.mean(valores)
print(statistica)

# obs: assim como a funcao mao a filter recebe um dois parametros, sendo uma funcao e um interavel
# obs: assim como na funcao map apos ser ultilizado os dados de filter eles sao excluidos da memoria
res = filter(lambda x: x > media,dados)
print(list(res))

paises = ['Brasil','','Argentina','chile']
print(paises)
respaises = filter(lambda pais: len(pais) > 0,paises)
print(list(respaises))


# Exemplo mais completo
usuarios = [
    {"username": "samuel", "tweets": ["Eu adodo bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

print(usuarios)

# Filtrar os usuários que estão inativos no Twitter
inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))

print(inativos)
