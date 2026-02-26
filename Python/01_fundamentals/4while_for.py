# ============================================================
# AULA: LOOPS (WHILE e FOR)
# ============================================================

# Loops servem para repetir uma ação várias vezes.
#
# Em Python temos dois principais:
# - while → usado quando NÃO sabemos exatamente quantas vezes vai repetir
# - for   → usado quando SABEMOS quantas vezes vai repetir


# ============================================================
# 1) WHILE
# ============================================================

# O while executa enquanto a condição for verdadeira.

contador = 1

while contador < 10:
    print(contador)
    contador += 1  # aumenta o valor do contador em 1

# Como funciona:
# 1) contador começa em 1
# 2) Python verifica: contador < 10 → True
# 3) Executa o bloco
# 4) Soma +1
# 5) Repete até contador chegar a 10
# 6) Quando a condição virar False, o loop para


# ============================================================
# LOOP INFINITO (CUIDADO)
# ============================================================

# Se você esquecer de atualizar o contador,
# o loop nunca vai parar.

# Exemplo (NÃO EXECUTE, pois será infinito):
#
# contador = 1
# while contador < 10:
#     print(contador)
#
# Aqui contador nunca muda,
# então a condição sempre será verdadeira.


# ============================================================
# QUANDO USAR WHILE?
# ============================================================

# Use when você NÃO sabe quantas vezes vai repetir.
#
# Exemplos reais:
# - Enquanto o usuário não digitar "sair"
# - Enquanto a senha estiver incorreta
# - Enquanto o saldo for maior que zero


# ============================================================
# 2) FOR
# ============================================================

# O for é usado quando sabemos quantas vezes queremos repetir.
# Ele normalmente usa a função range().


# ------------------------------------------------------------
# Exemplo 1: range(5)
# ------------------------------------------------------------

for numero in range(5):
    print("Executou")
    print(numero)

# range(5) cria uma sequência:
# 0, 1, 2, 3, 4
#
# Sempre começa do zero por padrão.
# Executa 5 vezes.


# ------------------------------------------------------------
# Exemplo 2: Definindo início e fim
# ------------------------------------------------------------

for numero_a in range(5, 10):
    print(numero_a)

# A sequência será:
# 5, 6, 7, 8, 9
#
# O número final (10) NÃO é incluído.


# ------------------------------------------------------------
# Exemplo 3: Definindo passo
# ------------------------------------------------------------

for numero in range(0, 10, 2):
    print(numero)

# Saída:
# 0, 2, 4, 6, 8
#
# Estrutura do range:
# range(inicio, fim, passo)


# ============================================================
# COMPARAÇÃO PRÁTICA
# ============================================================

# Mostrar números de 1 a 5 usando WHILE:

contador = 1
while contador <= 5:
    print(contador)
    contador += 1


# Mostrar números de 1 a 5 usando FOR:

for numero in range(1, 6):
    print(numero)


# ============================================================
# DIFERENÇA PRINCIPAL
# ============================================================

# WHILE:
# - Baseado em condição
# - Pode gerar loop infinito
# - Ideal quando não sabemos o limite exato

# FOR:
# - Baseado em sequência
# - Mais controlado
# - Ideal quando sabemos quantas vezes repetir


# ============================================================
# EXEMPLO PRÁTICO REAL
# ============================================================

# Exibir os 10 últimos posts de um sistema:
# Sabemos que serão 10 repetições → usamos for

for post in range(10):
    print(f"Exibindo post número {post + 1}")