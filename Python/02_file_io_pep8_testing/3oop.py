"""
PROJETO: Lista de Compras com Persistência em TXT (OOP)

Funcionalidades:
- Garantir que o ficheiro existe
- Ler lista existente
- Exibir itens
- Adicionar novos itens
- Verificar se um item já existe
- Comparar listas

Arquivo utilizado: shop_list.txt
"""


class ListaCompras:
    def __init__(self, arquivo):
        # Método construtor:
        # é executado automaticamente quando criamos um objeto da classe.
        # Aqui guardamos o nome do ficheiro e garantimos a sua existência.
        self.arquivo = arquivo
        self.garantir_arquivo()

    def garantir_arquivo(self):
        # Cria o ficheiro caso ele não exista.
        # O modo "a" (append) cria o ficheiro sem apagar o conteúdo.
        with open(self.arquivo, "a"):
            pass

    def ler_lista(self):
        # Lê o ficheiro e devolve uma lista com os itens.
        with open(self.arquivo, "r") as arquivo:
            lista = []
            for linha in arquivo:
                lista.append(linha.strip())
            return lista

    def exibir_lista(self):
        # Exibe os itens atuais da lista de compras.
        lista = self.ler_lista()

        print("\n= LISTA DE COMPRAS =")

        if not lista:
            print("Lista vazia.")
        else:
            for i, item in enumerate(lista, start=1):
                print(f"{i}. {item}")

        print()

    def adicionar_item(self, item):
        # Adiciona um novo item ao ficheiro.
        with open(self.arquivo, "a") as arquivo:
            arquivo.write(item + "\n")

    def item_existe(self, item):
        # Verifica se um item já está na lista.
        # lower() ajuda a comparar ignorando maiúsculas/minúsculas.
        lista = self.ler_lista()
        for item_lista in lista:
            if item_lista.lower() == item.lower():
                return True
        return False

    def comparar_listas(self, outra_lista):
        # Compara a lista do ficheiro com outra lista recebida por parâmetro.
        # Retorna os itens em comum.
        lista_atual = self.ler_lista()
        itens_iguais = []

        for item in lista_atual:
            if item in outra_lista:
                itens_iguais.append(item)

        return itens_iguais


# PROGRAMA PRINCIPAL
lista_compras = ListaCompras("shop_list.txt")

while True:
    lista_compras.exibir_lista()

    print("1 - Adicionar item")
    print("2 - Verificar se item existe")
    print("3 - Comparar com outra lista")
    print("4 - Sair")

    opcao = input("Escolha uma opcao: ").strip()

    if opcao == "1":
        novo_item = input("Digite o nome do item: ").strip()

        if novo_item:
            if lista_compras.item_existe(novo_item):
                print("Esse item ja existe na lista.\n")
            else:
                lista_compras.adicionar_item(novo_item)
                print("Item adicionado com sucesso!\n")
        else:
            print("Item invalido.\n")

    elif opcao == "2":
        item = input("Digite o item para verificar: ").strip()

        if lista_compras.item_existe(item):
            print("O item ja esta na lista.\n")
        else:
            print("O item nao esta na lista.\n")

    elif opcao == "3":
        # Exemplo simples de comparação com outra lista criada no código.
        outra_lista = ["arroz", "feijao", "leite", "cafe"]
        itens_em_comum = lista_compras.comparar_listas(outra_lista)

        print(f"Outra lista usada na comparacao: {outra_lista}")

        if itens_em_comum:
            print("Itens em comum:", itens_em_comum, "\n")
        else:
            print("Nao ha itens em comum.\n")

    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print("Opcao invalida.\n")

# ANTES #
# No modelo procedural, tu tinhas:
# variáveis soltas
# funções separadas
# o ficheiro controlado por uma variável global (ARQUIVO)

# AGORA #
# No modelo orientado a objetos, nós agrupamos tudo dentro da classe ListaCompras.
# Isso melhora porque:
# o código fica mais organizado
# as responsabilidades ficam centralizadas
# o objeto já “sabe” com que ficheiro está a trabalhar
# facilita reutilização e manutenção