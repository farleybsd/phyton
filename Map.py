"""
Map
Com o mao fazemos mapeamento de  valor para funcao
"""
import math
def area(r):
    """ Calcula area de um circulo com o raio r"""
    return math.pi * (r**2)

print(area(2))

raios =[2,4,8,2,78,45,12]
areas = []

# Forma Mais Comum
for r in raios:
    areas.append(area(r))

print(areas)

# Forma 2 Map
# map e uma funcao que recebe dois parametros primeiro a funcao e o segundo o interavel
areas = map(area,raios)
print(list(areas))

# Forma 3 - Map Com Lambda
# Obs: Apos ultilizar a funcao mao da primeira ultlizacao do resultado ele zera
print(f"Forma 3 - Map Com Lambda{list(map(lambda r: math.pi * (r **2),raios))}")

cidades =[('Berlim',29),('Cairo',36),('BuenosAires',19)]
c_para_f = lambda dado: (dado[0],(9/5) * dado[1] +32)
print(list(map(c_para_f,cidades)))