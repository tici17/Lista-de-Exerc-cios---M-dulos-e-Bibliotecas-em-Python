# Exercício 9 — Criando seu próprio módulo

import ematematica_basica

numero = float(input("Digite um número: "))

resultado_quadrado = ematematica_basica.quadrado(numero)
resultado_cubo = ematematica_basica.cubo(numero)

print("Quadrado:", resultado_quadrado)
print("Cubo:", resultado_cubo)