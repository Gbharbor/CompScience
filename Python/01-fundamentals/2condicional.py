"""
Estruturas Condicionais
"""

print("=== IF / ELIF / ELSE ===")

idade = int(input("Qual sua idade? "))

if idade == 17:
   print("Hora de alistar")
elif idade < 17:
   print("Cedo demais...")
else:
   print("Tarde demais...")


print("\n=== OPERADOR AND ===")

idade_user = int(input("Qual sua idade? "))

if 12 <= idade_user < 18:
   print("É um adolescente.")
elif idade_user >= 18:
   print("É um adulto.")
else:
   print("É uma criança.")


print("\n=== OPERADOR OR ===")

idade_user2 = int(input("Qual sua idade (alistamento)? "))

if idade_user2 == 17 or 21 <= idade_user2 < 25:
   print("Pode se alistar.")
elif idade_user2 >= 22:
   print("Não pode se alistar.")