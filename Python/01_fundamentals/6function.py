# ------------------------------------------
# 1) DEFINIÇÃO DE FUNÇÃO
# ------------------------------------------
# "def" vem de "definition" (definição)
# Aqui criamos (definimos) uma função chamada "somar"
# Ela recebe dois valores (parâmetros): x e y
def somar(x, y):
    # Dentro da função, fazemos a conta
    resultado = x + y

    # "return" devolve o valor para quem chamou a função
    return resultado


# ------------------------------------------
# 2) USANDO (CHAMANDO) A FUNÇÃO COM VALORES FIXOS
# ------------------------------------------
print("Minha primeira calculadora")

# Aqui estamos chamando a função "somar"
# e passando 10 e 8 como valores (argumentos)
# Esses valores substituem os parâmetros: x = 10 e y = 8
soma = somar(10, 8)

# Mostrando o resultado retornado
print(f"Total: {soma}")


# ------------------------------------------
# 3) USANDO (CHAMANDO) A FUNÇÃO COM INPUT DO USUÁRIO
# ------------------------------------------
# input() sempre retorna texto (string)
# por isso usamos int() para converter para número inteiro
numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

# Chamamos a função novamente, agora com os números digitados
soma = somar(numero1, numero2)

# Mostrando o resultado final
print(f"Resultado: {soma}")