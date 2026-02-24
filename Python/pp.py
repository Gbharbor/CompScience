# ============================================
# AULA: FUNDAMENTOS DE PYTHON
# ============================================

# --------------------------------------------
# 1) PRIMEIRO PROGRAMA: print()
# --------------------------------------------
# print() serve para mostrar mensagens na tela.

print("hello world")
print("hey, whats up")

# Para executar este arquivo no terminal:
# py fundamentos.py


# --------------------------------------------
# 2) VARIÁVEIS E TIPOS DE DADOS
# --------------------------------------------
# Em Python, você cria variáveis apenas atribuindo valores.

nome = "Harbor"   # string (texto)
idade = 90        # int (inteiro)
preco = 19.90     # float (decimal)

print(nome)
print(idade)
print(preco)


# --------------------------------------------
# 3) REATRIBUIÇÃO DE VARIÁVEL
# --------------------------------------------
# Python permite mudar o valor (e até o tipo) da mesma variável.

nome = "Harbor"
nome = 50   # Agora 'nome' deixou de ser string e virou inteiro.

print(nome)


# --------------------------------------------
# 4) DESCOBRIR O TIPO DA VARIÁVEL: type()
# --------------------------------------------
# type() mostra qual é o tipo atual da variável.

print(type(nome))   # int
print(type(preco))  # float


# --------------------------------------------
# 5) OPERAÇÕES ARITMÉTICAS
# --------------------------------------------
# Operadores básicos:
# +  soma
# -  subtração
# *  multiplicação
# /  divisão

resultado = 10 / 2

print(resultado)        # 5.0
print(type(resultado))  # float

# IMPORTANTE:
# A divisão (/) sempre retorna float,
# mesmo quando o resultado é exato.


# --------------------------------------------
# 6) SOMANDO NÚMEROS
# --------------------------------------------

number1 = 10
number2 = 5

soma = number1 + number2
print(soma)


# --------------------------------------------
# 7) CONVERSÃO DE TIPOS (CASTING)
# --------------------------------------------
# Às vezes o dado vem como texto, mas você precisa de número.
# Use int() para converter string numérica em inteiro.

number1 = 10
number2 = int("5")   # "5" (string) -> 5 (int)

soma = number1 + number2
print(soma)

# Se tentar converter algo que não é número, dá erro:
# int("Harbor")  -> ValueError


# --------------------------------------------
# 8) CONVERTER NÚMERO PARA STRING
# --------------------------------------------
# Também é possível fazer o contrário usando str().

name = str(10)

print(type(name))  # string
print(name)


# --------------------------------------------
# 9) RESUMO IMPORTANTE
# --------------------------------------------
# Python é dinamicamente tipado:
# - A variável não tem tipo fixo.
# - O tipo depende do valor atual.
# - A última atribuição é a que conta.

# Use sempre:
# type() -> para verificar o tipo
# int()  -> converter para inteiro
# str()  -> converter para texto