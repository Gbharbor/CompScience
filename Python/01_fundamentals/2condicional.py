# ============================================================
# AULA: ESTRUTURAS CONDICIONAIS
# ============================================================

# """
# Nesta aula você aprende:

# - Como usar if / elif / else
# - Operadores de comparação
# - Operadores lógicos (and / or)
# - Como condições retornam boolean (True ou False)
# """

# ============================================================
# 1) IF SIMPLES (==, <, >)
# ============================================================

# input() retorna string, então convertemos para int
idade = int(input("Qual sua idade? "))

if idade == 17:
    print("Hora de alistar")
elif idade < 17:
    print("Cedo demais...")
elif idade > 17:
    print("Tarde demais...")

# """
# Observação:
# Cada comparação gera um valor booleano (True ou False).

# Exemplos:

# 4 == 4   -> True
# 3 != 5   -> True
# 3 != 3   -> False
# 3 > 2    -> True
# 10 >= 20 -> False
# """

# ============================================================
# 2) OPERADORES DE COMPARAÇÃO
# ============================================================

# """
# ==   igual
# !=   diferente
# >    maior que
# <    menor que
# >=   maior ou igual
# <=   menor ou igual
# """

# ============================================================
# 3) OPERADOR LÓGICO AND
# ============================================================

# """
# AND exige que TODAS as condições sejam verdadeiras.
# """

idade_user = int(input("Qual sua idade? "))

if idade_user >= 12 and idade_user < 18:
    print("É um adolescente.")
elif idade_user >= 18:
    print("É um adulto.")
elif idade_user < 12:
    print("É uma criança.")


# ============================================================
# 4) OPERADOR LÓGICO OR
# ============================================================

# """
# OR exige que PELO MENOS UMA condição seja verdadeira.
# """

idade_user2 = int(input("Qual sua idade (alistamento)? "))

if idade_user2 == 17 or (idade_user2 >= 21 and idade_user2 < 25):
    print("Pode se alistar.")
elif idade_user2 >= 22:
    print("Não pode se alistar.")