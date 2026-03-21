"""
PROJETO: Lista de Compras com Persistência em TXT

Funcionalidades:
- Ler lista existente
- Exibir itens
- Adicionar novos itens
- Salvar no arquivo

Arquivo utilizado: shop_list.txt
"""

ARQUIVO = "shop_list.txt"

# 1. GARANTIR QUE O ARQUIVO EXISTE
# Abre o arquivo em modo append ("a") apenas para garantir a sua criação.
# Este modo cria o arquivo caso não exista e não altera o conteúdo existente.
with open(ARQUIVO, "a"):  
    pass  # instrução vazia: não executa nenhuma ação

# 2. FUNÇÃO PARA LER A LISTA
def ler_lista():
    # Abre o arquivo em modo leitura ("r")
    with open(ARQUIVO, "r") as arquivo:
        lista = []
        # Percorre cada linha do arquivo
        for linha in arquivo:
            # Remove espaços e quebras de linha (\n) antes de adicionar à lista
            lista.append(linha.strip())
        return lista

# 3. FUNÇÃO PARA EXIBIR A LISTA
def exibir_lista(lista):
    print("\n= LISTA DE COMPRAS =")
    
    if not lista:
        print("Lista vazia.")
    else:
        # enumerate permite percorrer a lista obtendo índice + valor
        # start=1 define que a contagem começa em 1 (mais adequado para exibição)
        for i, item in enumerate(lista, start=1):
            print(f"{i}. {item}")
    
    print()  # linha em branco para melhor organização visual

# 4. FUNÇÃO PARA ADICIONAR ITEM
def adicionar_item(item):
    # Abre o arquivo em modo append para adicionar conteúdo sem apagar o existente
    with open(ARQUIVO, "a") as arquivo:
        # Adiciona o item seguido de quebra de linha
        # Sem "\n", os itens ficariam todos na mesma linha
        arquivo.write(item + "\n")

# 5. LOOP PRINCIPAL
while True:  # loop contínuo até ser interrompido com break
    lista = ler_lista()
    exibir_lista(lista)

    print("1 - Add. Item")
    print("2 - Sair")

    # input permite ao utilizador introduzir dados pelo terminal
    # O valor digitado é armazenado como texto (string)
    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        # strip remove espaços em branco no início e fim do texto digitado
        novo_item = input("Digite o nome do item: ").strip()
        
        # Verifica se o utilizador realmente digitou algum conteúdo
        if novo_item:
            adicionar_item(novo_item)
            print("Item adicionado!\n")
        else:
            print("Item invalido.\n")

    elif opcao == "2":
        print("Saindo...")
        break  # encerra o loop

    else:
        print("Opcao invalida.\n")