"""
AULA: Manipulação de Arquivos em Python

Conteúdos abordados:
- Modos de abertura de arquivos (r, w, a, x)
- Leitura de arquivos
- Escrita em arquivos
- Adição de conteúdo (append)
- Uso do with open (boa prática)
"""

# ==========================================
# 1. MODOS DE ABERTURA DE ARQUIVOS
# ==========================================

# r = read (leitura)
# w = write (escrita - sobrescreve o arquivo)
# a = append (adiciona conteúdo ao final)
# x = create (cria arquivo novo e dá erro se já existir)


# ==========================================
# 2. ESCRITA EM ARQUIVO (WRITE)
# ==========================================

print("=== ESCRITA (WRITE) ===")

# Criando/escrevendo no arquivo
arquivo = open("arquivo_exemplo.txt", "w")

arquivo.write("Linha 1: Olá, mundo!\n")
arquivo.write("Linha 2: Aprendendo Python\n")

# Lista de nomes (precisa do \n para quebrar linha)
lista = ["Gui\n", "Ana\n", "Mari\n"]

arquivo.writelines(lista)

arquivo.close()  # SEMPRE fechar quando não usar "with"

print("Arquivo criado e escrito com sucesso!\n")


# ==========================================
# 3. LEITURA DE ARQUIVO (READ)
# ==========================================

print("=== LEITURA (READ) ===")

arquivo = open("arquivo_exemplo.txt", "r")

# Lendo linha por linha
linhas = arquivo.readlines()

for linha in linhas:
    print(f"Linha: {linha.strip()}")  # strip remove \n

arquivo.close()

print()


# ==========================================
# 4. ADICIONANDO CONTEÚDO (APPEND)
# ==========================================

print("=== APPEND (ADICIONAR) ===")

arquivo = open("arquivo_exemplo.txt", "a")

arquivo.write("Linha adicionada 1\n")
arquivo.write("Linha adicionada 2\n")

arquivo.close()

print("Conteúdo adicionado!\n")


# ==========================================
# 5. BOA PRÁTICA: WITH OPEN
# ==========================================

print("=== WITH OPEN (BOA PRÁTICA) ===")

# Leitura com with (não precisa fechar manualmente)
with open("arquivo_exemplo.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())

print()

# Escrita com with
with open("arquivo_exemplo.txt", "w") as arquivo:
    arquivo.write("Arquivo sobrescrito\n")
    arquivo.write("Novo conteúdo\n")

print("Arquivo reescrito com sucesso!")