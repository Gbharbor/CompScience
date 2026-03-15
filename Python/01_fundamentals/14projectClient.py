"""
=================================================
PROJETO: CADASTRO DE CLIENTES COM ENCAPSULAMENTO
=================================================

Regras:

1) Pessoa
   - nome
   - idade

2) Cliente herda de Pessoa
   - email
   - ltv

3) Usar encapsulamento:
   - atributos protegidos (_atributo)
   - getters e setters

4) Cadastrar 2 clientes em uma lista

5) Exibir os clientes cadastrados

6) Exibir soma total do LTV
"""


"""
========================================
1. Classe Pessoa
========================================
"""

class Pessoa:

    def __init__(self, nome, idade):

        # atributos protegidos
        self._nome = nome
        self._idade = idade


    """
    GETTERS
    """

    def get_nome(self):
        return self._nome

    def get_idade(self):
        return self._idade


    """
    SETTERS
    """

    def set_nome(self, novo_nome):
        self._nome = novo_nome

    def set_idade(self, nova_idade):
        self._idade = nova_idade



"""
========================================
2. Classe Cliente (herda de Pessoa)
========================================
"""

class Cliente(Pessoa):

    def __init__(self, nome, idade, email, ltv):

        # chama construtor da classe pai
        super().__init__(nome, idade)

        # novos atributos
        self._email = email
        self._ltv = float(ltv)


    """
    GETTERS
    """

    def get_email(self):
        return self._email

    def get_ltv(self):
        return self._ltv


    """
    SETTERS
    """

    def set_email(self, novo_email):
        self._email = novo_email

    def set_ltv(self, novo_ltv):
        self._ltv = float(novo_ltv)



"""
========================================
3. Criando lista de clientes
========================================
"""

clientes = []

clientes.append(Cliente("Ana", 20, "ana@gmail.com", 3000))
clientes.append(Cliente("Gui", 30, "gui@gmail.com", 2230))



"""
========================================
4. Exibindo clientes cadastrados
========================================
"""

soma_ltv = 0

for cliente in clientes:

    print(
        f"Nome: {cliente.get_nome()} | "
        f"Idade: {cliente.get_idade()} | "
        f"Email: {cliente.get_email()} | "
        f"LTV: ${cliente.get_ltv()}"
    )

    soma_ltv += cliente.get_ltv()



"""
========================================
5. Soma total do LTV
========================================
"""

print("------------")
print(f"TOTAL LTV: ${soma_ltv}")