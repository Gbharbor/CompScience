"""
AULA: Lidando com erros comuns em Python

OBJETIVO:
- Entender o que são erros em programação
- Diferenciar SyntaxError e RuntimeError
- Aprender o que é traceback
- Identificar e resolver erros comuns no código
- Desenvolver uma base melhor de depuração (debug)

--------------------------------------------------
1. INTRODUÇÃO

Durante a programação, é normal encontrar erros.
Esses erros podem acontecer de duas formas principais:

1) Antes do programa executar:
   - erros de sintaxe (SyntaxError)

2) Durante a execução do programa:
   - erros em tempo de execução (RuntimeError / exceções)

Além disso, quando ocorre um erro em tempo de execução,
o Python normalmente mostra um relatório chamado traceback.
"""
# --------------------------------------------------
# 2. SYNTAX ERROR
# --------------------------------------------------
"""
SyntaxError é um erro de sintaxe.

Isso significa que o código foi escrito de forma incorreta
e o Python nem consegue começar a execução.

Exemplos comuns:
- parênteses não fechados
- aspas não fechadas
- dois pontos ausentes
- indentação incorreta
"""

print("\n--- EXEMPLO 1: SyntaxError ---")

# EXEMPLO ERRADO (comentado para não quebrar o arquivo)
"""
print("Olá mundo"
"""

print("Exemplo corrigido: parenteses fechados corretamente.")


# --------------------------------------------------
# 3. ERRO DE INDENTAÇÃO
# --------------------------------------------------
"""
IndentationError também está relacionado à sintaxe.

Em Python, a indentação faz parte da estrutura do código.
Se ela estiver errada, o programa não executa.
"""

print("\n--- EXEMPLO 2: IndentationError ---")

# EXEMPLO ERRADO (comentado)
"""
if True:
print("Indentação incorreta")
"""

if True:
    print("Exemplo corrigido: indentação correta.")


# --------------------------------------------------
# 4. RUNTIME ERROR
# --------------------------------------------------
"""
Runtime Error é um erro que acontece DURANTE a execução.

Neste caso, o código está sintaticamente correto,
mas algo dá errado quando o programa roda.

Exemplos comuns:
- divisão por zero
- conversão inválida de tipos
- ficheiro não encontrado
- operação incompatível entre tipos
"""

print("\n--- EXEMPLO 3: Runtime Error ---")

try:
    numero = int(input("Digite um numero para dividir 10 por ele: "))
    resultado = 10 / numero
    print("Resultado:", resultado)

except Exception as e:
    print("Erro em tempo de execução:", e)


# --------------------------------------------------
# 5. TIPOS COMUNS DE ERROS EM TEMPO DE EXECUÇÃO
# --------------------------------------------------
print("\n--- EXEMPLO 4: Tipos comuns de erros ---")

# ValueError
try:
    valor = int("abc")
except ValueError:
    print("ValueError: nao foi possivel converter texto em numero.")

# ZeroDivisionError
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("ZeroDivisionError: nao e possivel dividir por zero.")

# TypeError
try:
    soma = "10" + 5
except TypeError:
    print("TypeError: nao e possivel somar tipos incompatíveis.")

# FileNotFoundError
try:
    with open("arquivo_que_nao_existe.txt", "r") as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print("FileNotFoundError: o ficheiro nao foi encontrado.")


# --------------------------------------------------
# 6. O QUE É TRACEBACK
# --------------------------------------------------
"""
Traceback é o relatório que o Python mostra quando ocorre um erro.

Ele indica:
- o caminho percorrido pelo programa até o erro
- a linha onde o erro aconteceu
- o tipo do erro
- a mensagem do erro

Regra importante:
-> O traceback normalmente deve ser lido de baixo para cima,
porque a última linha mostra o erro real.
"""

print("\n--- EXEMPLO 5: Explicação de traceback ---")

print("Quando ocorre um erro nao tratado, o Python mostra um traceback.")
print("O traceback ajuda a localizar a linha e o tipo do erro.")


# EXEMPLO DE TRACEBACK (apenas ilustrativo, em texto)
traceback_exemplo = """
Traceback (most recent call last):
  File "programa.py", line 10, in <module>
    resultado = 10 / 0
ZeroDivisionError: division by zero
"""

print("\nExemplo de traceback:")
print(traceback_exemplo)


# --------------------------------------------------
# 7. COMO INTERPRETAR UM TRACEBACK
# --------------------------------------------------
"""
Partes principais do traceback:

1) 'Traceback (most recent call last):'
   - indica que o relatório do erro começou

2) File "programa.py", line X
   - mostra o ficheiro e a linha do problema

3) Nome do erro no final
   - ex.: ZeroDivisionError, ValueError, TypeError

4) Mensagem do erro
   - explica o motivo do problema
"""

print("\n--- EXEMPLO 6: Como interpretar traceback ---")
print("Leia o traceback de baixo para cima.")
print("A última linha mostra o tipo do erro e a causa principal.")


# --------------------------------------------------
# 8. COMO IDENTIFICAR ERROS NO CÓDIGO
# --------------------------------------------------
"""
Passos recomendados para identificar erros:

1. Ler com atenção a mensagem de erro
2. Ver o tipo do erro
3. Observar a linha indicada
4. Analisar a lógica do código
5. Corrigir e testar novamente
"""

print("\n--- EXEMPLO 7: Processo de identificação de erros ---")
print("1. Leia a mensagem de erro")
print("2. Veja a linha indicada")
print("3. Entenda o tipo do erro")
print("4. Corrija o código")
print("5. Teste novamente")


# --------------------------------------------------
# 9. EXEMPLO DE ERRO E CORREÇÃO
# --------------------------------------------------
print("\n--- EXEMPLO 8: Erro e correcao ---")

# Exemplo com erro de tipo tratado
try:
    idade = input("Digite sua idade: ")
    print("Ano aproximado de nascimento:", 2025 - idade)

except TypeError:
    print("Erro: nao e possivel subtrair texto de numero.")

print("\nAgora a versão corrigida:")

try:
    idade = int(input("Digite sua idade novamente: "))
    print("Ano aproximado de nascimento:", 2025 - idade)

except ValueError:
    print("Erro: digite apenas numeros inteiros.")


# --------------------------------------------------
# 10. USANDO try/except PARA LIDAR COM ERROS
# --------------------------------------------------
"""
try:
    bloco onde o erro pode acontecer

except:
    bloco executado se o erro acontecer
"""

print("\n--- EXEMPLO 9: try/except ---")

try:
    numero = int(input("Digite um numero: "))
    print("Dobro do numero:", numero * 2)

except ValueError:
    print("Erro: o valor digitado nao e um numero valido.")


# --------------------------------------------------
# 11. USANDO except Exception
# --------------------------------------------------
"""
Exception é a classe base da maioria das exceções em Python.

Quando usamos:
except Exception as e

estamos capturando erros de forma mais genérica,
além de guardar o erro real na variável 'e'.
"""

print("\n--- EXEMPLO 10: except Exception ---")

try:
    numero = int(input("Digite um numero para dividir 20 por ele: "))
    resultado = 20 / numero
    print("Resultado:", resultado)

except Exception as e:
    print("Erro detectado:", e)


# --------------------------------------------------
# 12. BOAS PRÁTICAS AO LIDAR COM ERROS
# --------------------------------------------------
"""
Boas práticas:

- Ler o erro com atenção
- Não ignorar erros
- Preferir tratar erros específicos
- Usar mensagens claras
- Testar com diferentes entradas
- Corrigir uma coisa de cada vez
- Usar traceback como ferramenta de debug
"""

print("\n--- EXEMPLO 11: Boas práticas ---")
print("Sempre leia o erro antes de tentar corrigir.")
print("Prefira tratar erros específicos quando possível.")


# --------------------------------------------------
# 13. RESUMO FINAL
# --------------------------------------------------
"""
RESUMO:

1) SyntaxError
- erro na escrita do código
- impede a execução

2) RuntimeError / Exceções
- erro durante a execução
- pode acontecer mesmo com sintaxe correta

3) Traceback
- relatório detalhado do erro
- mostra a linha, o tipo e o caminho até o problema

4) try/except
- permite tratar erros e evitar que o programa quebre
"""

print("\n--- RESUMO FINAL ---")
print("SyntaxError -> erro de sintaxe")
print("RuntimeError -> erro durante a execução")
print("Traceback -> relatório detalhado do erro")
print("try/except -> tratamento de erros")


# --------------------------------------------------
# 14. MINI EXERCÍCIO
# --------------------------------------------------
"""
Exercício:
- pedir dois números ao utilizador
- fazer a divisão
- tratar erro se o utilizador digitar texto
- tratar erro se o divisor for zero
"""

print("\n--- MINI EXERCICIO ---")

try:
    n1 = int(input("Digite o primeiro numero: "))
    n2 = int(input("Digite o segundo numero: "))
    resultado = n1 / n2

except ValueError:
    print("Erro: digite apenas numeros.")

except ZeroDivisionError:
    print("Erro: nao e permitido dividir por zero.")

else:
    print("Resultado da divisao:", resultado)

finally:
    print("Fim do programa.")


# --------------------------------------------------
# FIM DA AULA
# --------------------------------------------------
print("\nAula finalizada.")