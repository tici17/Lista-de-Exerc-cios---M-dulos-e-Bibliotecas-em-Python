# Exercício 10 — Mini Projeto: Mega-Sena

import random

# Gera 6 números diferentes entre 1 e 60
numeros = random.sample(range(1, 61), 6)

# Coloca os números em ordem crescente
numeros.sort()

print("Números sorteados da Mega-Sena:")
print(numeros)