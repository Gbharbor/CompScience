"""
========================================
AULA: HERANÇA EM PROGRAMAÇÃO ORIENTADA A OBJETOS
========================================

Nesta aula aprendemos:

1) Como criar uma classe base.
2) Como criar métodos dentro da classe.
3) O que é HERANÇA.
4) Como uma classe pode herdar atributos e métodos de outra.
"""


"""
========================================
1. Criando uma Classe Base
========================================

Classe Pessoa representa uma pessoa
com dois atributos:

- nome
- idade
"""

class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    """
    Método da classe
    """

    def oi(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")



"""
========================================
2. Criando um objeto da classe
========================================
"""

p1 = Pessoa("Gui", 28)

# chamando o método da classe
p1.oi()



"""
========================================
3. O que é HERANÇA
========================================

Herança acontece quando uma classe
"herda" características de outra.

Por exemplo:

Funcionario pode herdar de Pessoa,
porque um funcionário também tem:

- nome
- idade

Assim não precisamos reescrever o código.
"""



"""
========================================
4. Criando uma Classe que HERDA de Pessoa
========================================
"""

class Funcionario(Pessoa):

    def __init__(self, nome, idade, salario):

        # chama o construtor da classe Pai (Pessoa)
        super().__init__(nome, idade)

        # novo atributo específico da classe Funcionario
        self.salario = salario


    """
    Método específico da classe Funcionario
    """

    def exibir_salario(self):
        print(f"Meu salário é {self.salario}")



"""
========================================
5. Criando um objeto da classe Funcionario
========================================
"""

f1 = Funcionario("Ana", 20, 3000)



"""
========================================
6. Usando métodos herdados
========================================

Mesmo não estando dentro da classe Funcionario,
o método "oi()" funciona porque foi herdado
da classe Pessoa.
"""

f1.oi()



"""
========================================
7. Usando método próprio da classe
========================================
"""

f1.exibir_salario()



"""
========================================
RESUMO DA AULA
========================================

Classe base:
Pessoa

Classe que herda:
Funcionario

Pessoa possui:
- nome
- idade
- método oi()

Funcionario herda:
- nome
- idade
- método oi()

Funcionario adiciona:
- salario
- método exibir_salario()

Benefícios da herança:

1) Reutilização de código
2) Organização
3) Estrutura hierárquica entre classes
"""