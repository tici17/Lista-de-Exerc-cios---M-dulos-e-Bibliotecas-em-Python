# Exercício 6 — Módulo random

import random

# a) Sorteia um número entre 1 e 100
numero = random.randint(1, 100)
print("Número sorteado:", numero)

# b) Lista com 5 filmes
filmes = [
    "Toy Story",
    "Harry Potter",
    "Homem-Aranha",
    "Vingadores",
    "A Pequena Sereia"
]

filme_escolhido = random.choice(filmes)
print("Filme escolhido:", filme_escolhido)

# c) Embaralha a lista
random.shuffle(filmes)
print("Lista de filmes embaralhada:", filmes)