"""
========================================
AULA: ENCAPSULAMENTO COM GETTERS E SETTERS
========================================

Nesta aula aprendemos:

1) Como criar uma classe em Python.
2) Como definir atributos dentro do método __init__.
3) O que são atributos públicos, protegidos e privados.
4) Como usar GETTERS e SETTERS para controlar o acesso aos atributos.
"""


"""
========================================
1. Criando uma Classe
========================================

Classe Product representa um produto com:
- nome
- preço
"""

class Product:

    """
    Método construtor (__init__)

    É executado automaticamente quando criamos
    um novo objeto da classe.
    """

    def __init__(self, name, price):
        # atributos protegidos (boa prática)
        self._name = name
        self._price = float(price)


    """
    ========================================
    2. GETTERS (métodos de leitura)
    ========================================
    Servem para acessar valores dos atributos
    de forma controlada.
    """

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price


    """
    ========================================
    3. SETTERS (métodos de modificação)
    ========================================
    Permitem alterar os atributos com controle.
    """

    def set_name(self, new_name):
        self._name = new_name

    def set_price(self, new_price):
        self._price = float(new_price)



"""
========================================
4. Criando Objetos (Instanciando a classe)
========================================
"""

p1 = Product("CD", 20)
p2 = Product("DVD", 40)



"""
========================================
5. Acessando atributos diretamente
========================================

Se os atributos forem públicos, podemos
acessar diretamente usando:
objeto.atributo
"""

print(p1._name)

# Podemos alterar diretamente
p1._name = "Pendrive"
print(p1._name)



"""
========================================
6. Acessando usando GETTERS
========================================

Forma mais segura e recomendada.
"""

print(p1.get_name())



"""
========================================
7. Alterando valores usando SETTERS
========================================
"""

p1.set_name("SSD")
print(p1.get_name())

p1.set_price(30)

print(f"O produto {p1.get_name()} agora custa {p1.get_price()}€")



"""
========================================
RESUMO DA AULA
========================================

Tipos de atributos em Python:

1) Público
   name
   Pode ser acessado diretamente.

2) Protegido
   _name
   Indica que não deveria ser acessado diretamente,
   mas Python ainda permite.

3) Privado
   __name
   Só pode ser acessado dentro da própria classe.

Para controlar acesso usamos:

GETTERS -> ler valores
SETTERS -> modificar valores
"""