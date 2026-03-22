"""
AULA: Tratamento de Exceções em Python

OBJETIVO:
- Entender o que são exceções
- Aprender try, except, else e finally
- Escrever código mais seguro e robusto
"""

# --------------------------------------------------
# 1. O QUE SÃO EXCEÇÕES?
# --------------------------------------------------
"""
Exceções são erros que acontecem DURANTE a execução do programa.

Exemplos:
- Divisão por zero
- Converter texto inválido para número
- Arquivo inexistente

Sem tratamento -> o programa quebra
Com tratamento -> o programa continua controlado

Exception = "captura tudo"
except Exception = genérico
except Exception as e = genérico + debug
"""


# --------------------------------------------------
# 2. EXEMPLO SEM TRATAMENTO (comentado para não quebrar o programa)
# --------------------------------------------------
"""
numero = int(input("Digite um numero: "))
resultado = 10 / numero
print(resultado)
"""

# Se o usuário digitar 0 ou texto -> ERRO


# --------------------------------------------------
# 3. USANDO TRY E EXCEPT (genérico)
# --------------------------------------------------
print("\n--- Exemplo 1: try/except genérico ---")

try:
    numero = int(input("Digite um numero: "))
    resultado = 10 / numero
    print("Resultado:", resultado)

except:
    print("Ocorreu um erro!")


# --------------------------------------------------
# 4. TRATANDO ERROS ESPECÍFICOS
# --------------------------------------------------
print("\n--- Exemplo 2: erros específicos ---")

try:
    numero = int(input("Digite um numero: "))
    resultado = 10 / numero
    print("Resultado:", resultado)

except ValueError:
    print("Erro: digite apenas numeros.")

except ZeroDivisionError:
    print("Erro: nao e possivel dividir por zero.")


# --------------------------------------------------
# 5. USANDO ELSE
# --------------------------------------------------
print("\n--- Exemplo 3: uso do else ---")

try:
    numero = int(input("Digite um numero: "))
    resultado = 10 / numero

except ValueError:
    print("Erro: entrada invalida.")

except ZeroDivisionError:
    print("Erro: divisao por zero.")

else:
    print("Resultado calculado com sucesso:", resultado)


# --------------------------------------------------
# 6. USANDO FINALLY
# --------------------------------------------------
print("\n--- Exemplo 4: uso do finally ---")

try:
    numero = int(input("Digite um numero: "))
    resultado = 10 / numero

except ValueError:
    print("Erro: entrada invalida.")

except ZeroDivisionError:
    print("Erro: divisao por zero.")

else:
    print("Resultado:", resultado)

finally:
    print("Fim da execucao (sempre executa).")


# --------------------------------------------------
# 7. EXEMPLO COM ARQUIVOS
# --------------------------------------------------
print("\n--- Exemplo 5: leitura de arquivo ---")

try:
    with open("dados.txt", "r") as arquivo:
        conteudo = arquivo.read()

except FileNotFoundError:
    print("Erro: arquivo nao encontrado.")

else:
    print("Conteudo do arquivo:")
    print(conteudo)

finally:
    print("Operacao com arquivo finalizada.")


# --------------------------------------------------
# 8. MULTIPLOS ERROS EM UM EXCEPT
# --------------------------------------------------
print("\n--- Exemplo 6: múltiplos erros ---")

try:
    numero = int(input("Digite um numero: "))
    resultado = 10 / numero
    print("Resultado:", resultado)

except (ValueError, ZeroDivisionError):
    print("Erro: entrada invalida ou divisao por zero.")


# --------------------------------------------------
# 9. CAPTURANDO O ERRO (DEBUG)
# --------------------------------------------------
print("\n--- Exemplo 7: capturando erro ---")

try:
    numero = int(input("Digite um numero: "))
    resultado = 10 / numero
    print("Resultado:", resultado)

except Exception as e:
    print("Erro detectado:", e)


# --------------------------------------------------
# 10. RESUMO FINAL (IMPORTANTE)
# --------------------------------------------------
"""
try:
    # código que pode dar erro

except:
    # executa se houver erro

else:
    # executa se NÃO houver erro

finally:
    # executa sempre
"""


# --------------------------------------------------
# 11. EXERCÍCIO
# --------------------------------------------------
print("\n--- Mini exercício ---")

try:
    n1 = int(input("Digite o primeiro numero: "))
    n2 = int(input("Digite o segundo numero: "))
    resultado = n1 / n2

except ValueError:
    print("Erro: digite apenas numeros.")

except ZeroDivisionError:
    print("Erro: divisao por zero.")

else:
    print("Resultado da divisao:", resultado)

finally:
    print("Programa finalizado.")
