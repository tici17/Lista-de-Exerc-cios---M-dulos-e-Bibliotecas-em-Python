# Exercício 7 — Módulo datetime

from datetime import datetime

agora = datetime.now()

print("Data e hora atuais:", agora)
print("Data no formato brasileiro:", agora.strftime("%d/%m/%Y"))