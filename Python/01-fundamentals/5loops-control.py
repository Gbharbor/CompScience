"""
Listas e Controle de Loops
"""

print("=== LISTA DE NOMES ===")

nomes = ["joao", "ana", "Gui", "Ju"]

print("Inscricoes:")

for nome in nomes:
   print(f"Nome inscrito: {nome.title()}")

print("- Obrigado pela inscricao!")


print("\n=== TABUADA ===")

tabuada = [1,2,3,4,5,6,7,8,9,10]

for numero in tabuada:
   print(f"{numero} x 2 = {numero * 2}")


print("\n=== LOOP EM STRING ===")

for letra in "Python":
   print(letra)