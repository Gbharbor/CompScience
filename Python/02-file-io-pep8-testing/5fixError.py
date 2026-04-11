"""
Lidando com Erros Comuns em Python
"""

print("\n=== SYNTAX ERROR ===")
print("SyntaxError acontece quando o codigo foi escrito de forma incorreta.")
print("Exemplo corrigido: parenteses fechados corretamente.")


print("\n=== INDENTATION ERROR ===")

if True:
   print("Exemplo corrigido: indentacao correta.")


print("\n=== RUNTIME ERROR ===")

try:
   numero = int(input("Digite um numero para dividir 10 por ele: "))
   print("Resultado:", 10 / numero)

except Exception as e:
   print("Erro em tempo de execucao:", e)


print("\n=== TIPOS COMUNS DE ERROS ===")

try:
   int("abc")
except ValueError:
   print("ValueError: nao foi possivel converter texto em numero.")

try:
   10 / 0
except ZeroDivisionError:
   print("ZeroDivisionError: nao e possivel dividir por zero.")

try:
   "10" + 5
except TypeError:
   print("TypeError: nao e possivel operar tipos incompativeis.")

try:
   with open("arquivo_que_nao_existe.txt", "r") as arquivo:
      print(arquivo.read())
except FileNotFoundError:
   print("FileNotFoundError: o ficheiro nao foi encontrado.")


print("\n=== TRACEBACK ===")

traceback_exemplo = """
Traceback (most recent call last):
File "programa.py", line 10, in <module>
   resultado = 10 / 0
ZeroDivisionError: division by zero
"""

print("Quando ocorre um erro nao tratado, o Python mostra um traceback.")
print("Leia o traceback de baixo para cima.")
print(traceback_exemplo)


print("\n=== IDENTIFICANDO ERROS ===")
print("1. Leia a mensagem de erro")
print("2. Veja a linha indicada")
print("3. Entenda o tipo do erro")
print("4. Corrija o codigo")
print("5. Teste novamente")


print("\n=== ERRO E CORRECAO ===")

try:
   idade = input("Digite sua idade: ")
   print("Ano aproximado de nascimento:", 2025 - idade)

except TypeError:
   print("Erro: nao e possivel subtrair texto de numero.")

print("\nVersao corrigida:")

try:
   idade = int(input("Digite sua idade novamente: "))
   print("Ano aproximado de nascimento:", 2025 - idade)

except ValueError:
   print("Erro: digite apenas numeros inteiros.")


print("\n=== TRY / EXCEPT ===")

try:
   numero = int(input("Digite um numero: "))
   print("Dobro do numero:", numero * 2)

except ValueError:
   print("Erro: o valor digitado nao e um numero valido.")


print("\n=== EXCEPTION AS E ===")

try:
   numero = int(input("Digite um numero para dividir 20 por ele: "))
   print("Resultado:", 20 / numero)

except Exception as e:
   print("Erro detectado:", e)


print("\n=== BOAS PRATICAS ===")
print("Sempre leia o erro antes de tentar corrigir.")
print("Prefira tratar erros especificos quando possivel.")


print("\n=== RESUMO FINAL ===")
print("SyntaxError -> erro de sintaxe")
print("RuntimeError -> erro durante a execucao")
print("Traceback -> relatorio detalhado do erro")
print("try/except -> tratamento de erros")


print("\n=== MINI EXERCICIO ===")

try:
   n1 = int(input("Digite o primeiro numero: "))
   n2 = int(input("Digite o segundo numero: "))
   print("Resultado da divisao:", n1 / n2)

except ValueError:
   print("Erro: digite apenas numeros.")

except ZeroDivisionError:
   print("Erro: nao e permitido dividir por zero.")

finally:
   print("Fim do programa.")


print("\nAula finalizada.")