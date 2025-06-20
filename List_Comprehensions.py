"""
https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
Compreensões de lista fornecem uma maneira concisa de criar listas.
Aplicações comuns incluem a criação de novas listas em que cada elemento
é o resultado de algumas operações aplicadas a cada membro de outra sequência
ou iterável, ou a criação de uma subsequência desses elementos que satisfazem
uma determinada condição.

Podemos Gerar novas Listas com dados processados a paetir de outro interavel

Comprehensions em Python ≈ LINQ com select, where e ToList() em C#
Python	C#                                (LINQ)
[x for x in lista]	                      .Select(x => x)
[x for x in lista if cond]	              .Where(cond).Select(x => x)
{k: v for ...}	                          .ToDictionary(k => ..., v => ...)
{x for x in ...}	                       new HashSet<T>(...)
(x for x in ...)	                       .Select(x => x) (como IEnumerable)
"""

#List comprehension em Python:

quadrados = [x**2 for x in range(5)]
print(f"✅List comprehension em Python {quadrados}")

# var quadrados = Enumerable.Range(0, 5).Select(x => x * x).ToList();
# var quadrados = Enumerable.Range(0, 5).Select(x => x * x).ToList();

#✅ Com filtro (if) em Python:
pares = [x for x in range(10) if x % 2 == 0]
#var pares = Enumerable.Range(0, 10).Where(x => x % 2 == 0).ToList();
print(f"✅ Com filtro (if) em Python: {pares}")

# Dict comprehension em Python:

nomes = ['Ana', 'Beto']
idades = [25, 30]
dicionario = {nome: idade for nome, idade in zip(nomes, idades)}
nomes = ['Ana', 'Beto']
idades = [25, 30]
dicionario = {nome: idade for nome, idade in zip(nomes, idades)}
print(f" ✅ Dict comprehension em Python: {dicionario}")

#var nomes = new[] { "Ana", "Beto" };
#var idades = new[] { 25, 30 };
#var dicionario = nomes.Zip(idades, (nome, idade) => new { nome, idade })
#                      .ToDictionary(x => x.nome, x => x.idade);


#✅ Set comprehension em Python:

unicos = {x for x in [1, 2, 2, 3]}
print(f'✅ Set comprehension em Python:: {unicos}')
#var unicos = new HashSet<int>(new[] { 1, 2, 2, 3 });
