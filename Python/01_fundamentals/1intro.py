# ============================================================
# AULA COMPLETA: FUNDAMENTOS + INPUT + STRINGS
# ============================================================
#
#Este arquivo reúne:

#Aula 1:
#- print()
#- variáveis
#- tipos
#- reatribuição
#- operações aritméticas
#- type()
#- casting (int / str)

#Aula 2:
#- input()
#- conversão de tipos
#- concatenação
#- f-strings
#- métodos de string
#- len()

#Tudo organizado de forma progressiva.


# ============================================================
# 1) PRIMEIRO PROGRAMA
# ============================================================

print("hello world")

# ============================================================
# 2) VARIÁVEIS E TIPOS DE DADOS
# ============================================================

nome = "Harbor"   # string (texto)
idade = 90        # int (inteiro)
preco = 19.90     # float (decimal)

print(nome)
print(idade)
print(preco)


# ============================================================
# 3) REATRIBUIÇÃO DE VARIÁVEL
# ============================================================

# Python é dinamicamente tipado.
# O tipo depende do valor atual da variável.

nome = "Harbor"
nome = 50  # agora virou inteiro

print(nome)
print(type(nome))   # int
print(type(preco))  # float


# ============================================================
# 4) OPERAÇÕES ARITMÉTICAS
# ============================================================

resultado = 10 / 2

print(resultado)        # 5.0
print(type(resultado))  # float

# Divisão (/) sempre retorna float.

number1 = 10
number2 = 5

soma = number1 + number2
print(soma)


# ============================================================
# 5) CONVERSÃO DE TIPOS (CASTING)
# ============================================================

number1 = 10
number2 = int("5")  # string -> inteiro

soma = number1 + number2
print(soma)

# Converter número para string:
name = str(10)
print(type(name))


# ============================================================
# 6) INPUT (ENTRADA DE DADOS)
# ============================================================

"""
input() SEMPRE retorna string.
Mesmo que o usuário digite números.
"""

user_name = input("Qual seu nome? ")
user_name = user_name.title()  # primeira letra maiúscula

user_age = input("Qual sua idade? ")
user_age = int(user_age)  # convertendo para inteiro


# ============================================================
# 7) CONCATENAÇÃO (FORMA ANTIGA)
# ============================================================

print("Nome: " + user_name)
print("Idade: " + str(user_age))

print("O seu nome é " + user_name + " e você tem " + str(user_age) + " anos.")


# ============================================================
# 8) F-STRINGS (FORMA MODERNA)
# ============================================================

numero = 10 + 5  # expressão

print(
    f"O seu nome é {user_name} "
    f"({len(user_name)} caracteres) "
    f"e você tem {user_age} anos. "
    f"Eu gosto do número {numero}. "
    f"Posso calcular 10+2 aqui mesmo: {10+2}. "
    f"Daqui 10 anos você terá: {user_age + 10}."
)


# ============================================================
# 9) MÉTODOS DE STRING
# ============================================================

texto = "algo"

print(texto.upper())  # maiúsculo
print(texto.lower())  # minúsculo
print(texto.title())  # primeira letra maiúscula

print(f"O nome tem {len(user_name)} caracteres.")


# ============================================================
# 10) RESUMO GERAL
# ============================================================

# """
# ✔ Python é dinamicamente tipado.
# ✔ input() sempre retorna string.
# ✔ Para fazer contas com números digitados, use int().
# ✔ Para juntar texto com número usando +, use str().
# ✔ f-strings são a forma moderna de formatação.
# ✔ Métodos de string usam ponto (.upper(), .lower(), .title()).
# ✔ len() conta caracteres.
# """