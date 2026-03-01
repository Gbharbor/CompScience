# ============================================================
# USO DE LISTAS E DICIONÁRIOS EM PYTHON PARA MODELAR DADOS
# (ex.: usuários, posts, produtos, etc.)
# ============================================================

# --------------------------------------------
# 1) Lista simples (somente strings)
# --------------------------------------------
lista = ["gui", "joao"]
print("Lista simples:", lista)
print("-" * 40)

# --------------------------------------------
# 2) Dicionários (um usuário por dicionário)
# --------------------------------------------
# Cada usuário pode ser representado como um dicionário:
# usuario1 = {"nome": "gui", "idade": 20}
# usuario2 = {"nome": "ana", "idade": 30}

# --------------------------------------------
# 3) Lista de dicionários (modelo mais comum)
# --------------------------------------------
# Aqui você cria uma lista onde cada item é um dicionário (um usuário)
usuarios = [
    {"nome": "gui", "idade": 20},
    {"nome": "ana", "idade": 30},
]

print("Usuários iniciais:", usuarios)
print("-" * 40)

# --------------------------------------------
# 4) Adicionando um novo usuário com .append()
# --------------------------------------------
# Você pode adicionar direto, sem criar variável:
usuarios.append({"nome": "fulano", "idade": 90})

print("Depois do append:", usuarios)
print("-" * 40)

# --------------------------------------------
# 5) Adicionando usuários via função (melhor para reutilizar)
# --------------------------------------------
# Vantagem: você padroniza e evita repetir código.

def novo_usuario(nome, idade):
    """
    Adiciona um novo usuário na lista 'usuarios'.
    - nome: string
    - idade: int
    """
    usuarios.append({"nome": nome, "idade": idade})

# Chamando a função para adicionar mais usuários:
novo_usuario("Ciclano", 30)
novo_usuario("Guilherme", 340)

print("Depois de adicionar via função:", usuarios)
print("-" * 40)

# --------------------------------------------
# 6) Percorrendo a lista e exibindo os dados
# --------------------------------------------
# Cada 'usuario' aqui é um dicionário (com chaves "nome" e "idade").
for usuario in usuarios:
    # Atenção às aspas: usamos aspas simples dentro do dicionário
    print(f"{usuario['nome']} tem {usuario['idade']} anos.")

print("-" * 40)

# --------------------------------------------
# 7) Mostrando a lista completa no final (debug / conferência)
# --------------------------------------------
print("Lista final de usuários:", usuarios)