# ==========================================================
# AULA: INTRODUÇÃO A CLASSES EM PYTHON
# ==========================================================
#
# Nesta aula vamos aprender:
#
# 1) O que são classes
# 2) O que são atributos
# 3) O que são métodos
# 4) O que é instanciar um objeto
# 5) O que é um construtor (__init__)
#
# ----------------------------------------------------------
# EXEMPLO CONCEITUAL
#
# Imagine um sistema de cadastro de usuários.
#
# ENTIDADE: Usuário
#
# ATRIBUTOS:
# - nome
# - email
# - senha
#
# MÉTODOS:
# - login()
# - logout()
# - change_password()
#
# Criar um usuário significa criar um OBJETO da classe.
# Esse processo chama-se INSTANCIAR.
#
# Classes servem para organizar melhor o código.
# ==========================================================


# ==========================================================
# 1) EXEMPLO SIMPLES SEM USAR CLASSES
# ==========================================================
# Neste exemplo usamos apenas variáveis e funções.


nome = "Carlos"
idade = 18


def apresentar(nome, idade):
    print(f"Olá, eu sou {nome} e tenho {idade} anos.")


print("EXEMPLO SEM CLASSES")
apresentar(nome, idade)


# ----------------------------------------------------------
# Problema:
# Se tivermos muitos utilizadores, o código fica desorganizado.
#
# nome1
# idade1
#
# nome2
# idade2
#
# nome3
# idade3
#
# Para resolver isso usamos CLASSES.
# ==========================================================


print("\n----------------------------")
print("INTRODUÇÃO ÀS CLASSES")
print("----------------------------")


# ==========================================================
# 2) CRIANDO UMA CLASSE
# ==========================================================
#
# Convenção em Python:
# Classes começam com letra MAIÚSCULA.
#
# Uma classe funciona como um MOLDE para criar objetos.


class Product:
    pass


# Neste momento apenas criámos o molde.
# Ainda não criámos nenhum produto.


# ==========================================================
# 3) ADICIONANDO ATRIBUTOS COM O CONSTRUTOR
# ==========================================================
#
# O construtor é uma função especial chamada automaticamente
# quando criamos um objeto da classe.
#
# O nome do construtor em Python é:
#
# __init__


class Product:

    def __init__(self, name, price):
        # self representa o próprio objeto

        self.name = name
        self.price = price


# ==========================================================
# 4) CRIANDO MÉTODOS
# ==========================================================
#
# Métodos são funções que pertencem à classe.


class Product:

    def __init__(self, name, price):

        self.name = name
        self.price = price

    def resumir(self):

        print(f"{self.name} custa {self.price}")


# ==========================================================
# 5) CRIANDO OBJETOS (INSTÂNCIAS)
# ==========================================================
#
# Agora vamos usar a classe para criar produtos.


print("\nCRIANDO PRODUTOS")


p1 = Product("CD usando construtor", 20)
p2 = Product("DVD usando construtor", 40)


# ==========================================================
# 6) UTILIZANDO MÉTODOS
# ==========================================================

p1.resumir()
p2.resumir()


# Saída esperada:
#
# CD usando construtor custa 20
# DVD usando construtor custa 40


# ==========================================================
# 7) FORMA ANTIGA (SEM CONSTRUTOR)
# ==========================================================
#
# O professor mostrou que poderíamos fazer assim:


# p1 = Product()
# p1.name = "CD"
# p1.price = 20


# Mas isso não é recomendado.
# O ideal é usar __init__ para garantir que o objeto
# já nasce com todos os dados necessários.


# ==========================================================
# RESUMO DA AULA
# ==========================================================
#
# CLASSE
# -> modelo para criar objetos
#
# ATRIBUTOS
# -> características do objeto
#
# MÉTODOS
# -> ações que o objeto pode executar
#
# INSTÂNCIA
# -> objeto criado a partir da classe
#
# CONSTRUTOR
# -> função executada quando o objeto é criado
#
# Analogia:
#
# Classe = molde de bolo
# Objeto = bolo pronto
#
# class Product -> molde
# p1 = Product() -> bolo criado
#
# ==========================================================