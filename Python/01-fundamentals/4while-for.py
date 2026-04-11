"""
Loops: while e for
"""

print("=== WHILE ===")

contador = 1

while contador < 10:
   print(contador)
   contador += 1


print("\n=== FOR COM RANGE(5) ===")

for numero in range(5):
   print("Executou")
   print(numero)


print("\n=== FOR COM INICIO E FIM ===")

for numero in range(5, 10):
   print(numero)


print("\n=== FOR COM PASSO ===")

for numero in range(0, 10, 2):
   print(numero)


print("\n=== COMPARACAO: 1 A 5 COM WHILE ===")

contador = 1

while contador <= 5:
   print(contador)
   contador += 1


print("\n=== COMPARACAO: 1 A 5 COM FOR ===")

for numero in range(1, 6):
   print(numero)


print("\n=== EXEMPLO PRATICO ===")

for post in range(10):
   print(f"Exibindo post numero {post + 1}")