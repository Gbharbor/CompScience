# """
# =========================================================
# ESTRUTURAS DE DADOS EM PYTHON
# Listas | Tuplas | Dicionários
# =========================================================
# """

print("========== LISTAS ==========\n")

# -------------------------------------------------------
# 1) LISTAS
# -------------------------------------------------------
# Listas são estruturas MUTÁVEIS (podem ser alteradas)
# São criadas com colchetes []

lista1 = ["arroz", "feijao", "carne"]
lista2 = ["ana", "ju", "gui"]
lista3 = ["arroz", 1, "gui", "bla"]  # pode misturar tipos

print("Lista1 original:", lista1)
print("Lista2:", lista2)
print("Lista3 (tipos mistos):", lista3)

# -------------------------------------------------------
# ACESSANDO ELEMENTOS (ÍNDICE)
# -------------------------------------------------------
# Toda lista começa no índice 0

print("\nPrimeiro elemento da lista2:", lista2[0])
print("Segundo elemento da lista1:", lista1[1])

# -------------------------------------------------------
# ALTERANDO ELEMENTOS
# -------------------------------------------------------
# Como lista é mutável, podemos alterar valores

lista1[1] = "lentilha"  # trocando feijao por lentilha
print("\nLista1 após alteração:", lista1)


print("\n========== TUPLAS ==========\n")

# -------------------------------------------------------
# 2) TUPLAS
# -------------------------------------------------------
# Tuplas são estruturas IMUTÁVEIS (não podem ser alteradas)
# São criadas com parênteses ()

tupla1 = ("arroz", "feijao", "carne")

print("Tupla1:", tupla1)

# Acessando elemento
print("Primeiro elemento da tupla:", tupla1[0])

# -------------------------------------------------------
# TENTATIVA DE MODIFICAÇÃO (GERARIA ERRO)
# -------------------------------------------------------
# tupla1[1] = "batata"
# Isso daria erro porque tuplas não podem ser modificadas


print("\n========== DICIONÁRIOS ==========\n")

# -------------------------------------------------------
# 3) DICIONÁRIOS
# -------------------------------------------------------
# Estrutura chave: valor
# São criados com chaves {}

pessoa = {
    "nome": "gui",
    "idade": 90,
    "pais": "Brasil"
}

print("Dicionário completo:", pessoa)

# -------------------------------------------------------
# ACESSANDO VALORES
# -------------------------------------------------------
# Diferente da lista, aqui acessamos pela CHAVE

print("\nNome:", pessoa["nome"])
print("Idade:", pessoa["idade"])

# -------------------------------------------------------
# ALTERANDO VALORES
# -------------------------------------------------------

pessoa["idade"] = 100
print("\nIdade após atualização:", pessoa["idade"])

# -------------------------------------------------------
# ADICIONANDO NOVO ITEM
# -------------------------------------------------------

pessoa["profissao"] = "Engenharia"
print("\nDicionário após adicionar profissão:", pessoa)


print("\n========== RESUMO FINAL ==========\n")

print("Lista -> Usa [] | Pode alterar | Acesso por índice")
print("Tupla -> Usa () | NÃO pode alterar | Acesso por índice")
print("Dicionário -> Usa {} | Pode alterar | Acesso por chave")