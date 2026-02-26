# ============================================================
# AULA: LISTAS E CONTROLE DE LOOPS
# ============================================================

# Listas são estruturas de dados que armazenam múltiplos valores.
# Elas são definidas com colchetes: [ ]

# ============================================================
# 1) LISTA DE NOMES
# ============================================================

# Criando uma lista
lista = ["joao", "ana", "Gui", "Ju"]

# Exibindo um título antes do loop
print("Inscrições:")

# O for percorre automaticamente todos os itens da lista.
# O Python já sabe quantos elementos existem nela.
for name in lista:
    print(f"Nomes inscritos: {name.title()}")

print("- Obrigado pela inscrição!")


# ============================================================
# COMO O FOR FUNCIONA COM LISTAS?
# ============================================================

# Para cada item dentro da lista:
# 1) O Python pega o primeiro valor
# 2) Atribui à variável "name"
# 3) Executa o bloco
# 4) Passa para o próximo item
# 5) Repete até acabar a lista

# Não precisamos usar contador.
# O for já controla isso automaticamente.


# ============================================================
# 2) LISTA NUMÉRICA (TABUADA)
# ============================================================

tabuada = [1,2,3,4,5,6,7,8,9,10]

for numero in tabuada:
    print(f"{numero} x 2 = {numero * 2}")

# O loop percorre cada número da lista.
# Em cada repetição:
# - "numero" recebe um valor da lista
# - Executa a multiplicação
# - Mostra o resultado


# ============================================================
# CONCEITO IMPORTANTE
# ============================================================

# O for em Python não percorre apenas números.
# Ele percorre qualquer sequência:
#
# - listas
# - strings
# - range()
# - tuplas
# - dicionários (mais adiante)

# Exemplo percorrendo uma string:

for letra in "Python":
    print(letra)