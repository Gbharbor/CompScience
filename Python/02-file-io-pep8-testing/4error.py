"""
Tratamento de Exceções em Python
"""

print("\n=== TRY / EXCEPT (genérico) ===")
try:
   numero = int(input("Digite um numero: "))
   print("Resultado:", 10 / numero)
except:
   print("Ocorreu um erro!")


print("\n=== ERROS ESPECÍFICOS ===")
try:
   numero = int(input("Digite um numero: "))
   print("Resultado:", 10 / numero)

except ValueError:
   print("Erro: digite apenas numeros.")

except ZeroDivisionError:
   print("Erro: nao e possivel dividir por zero.")


print("\n=== ELSE ===")
try:
   numero = int(input("Digite um numero: "))
   resultado = 10 / numero

except ValueError:
   print("Erro: entrada invalida.")

except ZeroDivisionError:
   print("Erro: divisao por zero.")

else:
   print("Resultado:", resultado)


print("\n=== FINALLY ===")
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
   print("Fim da execucao.")


print("\n=== ARQUIVOS ===")
try:
   with open("dados.txt", "r") as arquivo:
      print(arquivo.read())

except FileNotFoundError:
   print("Erro: arquivo nao encontrado.")

finally:
   print("Operacao finalizada.")


print("\n=== MULTIPLOS ERROS ===")
try:
   numero = int(input("Digite um numero: "))
   print("Resultado:", 10 / numero)

except (ValueError, ZeroDivisionError):
   print("Erro: entrada invalida ou divisao por zero.")


print("\n=== DEBUG ===")
try:
   numero = int(input("Digite um numero: "))
   print("Resultado:", 10 / numero)

except Exception as e:
   print("Erro detectado:", e)


print("\n=== EXERCICIO ===")
try:
   n1 = int(input("Digite o primeiro numero: "))
   n2 = int(input("Digite o segundo numero: "))
   print("Resultado:", n1 / n2)

except ValueError:
   print("Erro: digite apenas numeros.")

except ZeroDivisionError:
   print("Erro: divisao por zero.")

finally:
   print("Programa finalizado.")