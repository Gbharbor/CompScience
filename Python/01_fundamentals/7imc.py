# Tabela IMC:
# Abaixo de 19.1: abaixo do peso
# Entre 19.1 e 25.8: peso normal
# Entre 25.9 e 27.3: pouco acima do peso
# Entre 27.4 e 32.3: acima do peso
# Acima de 32.4: obesidade

# Fórmula do IMC: peso / (altura * altura)
def calc_imc(peso, altura):
   imc = peso / (altura * altura)
   return imc 

peso = float(input("digite seu peso(em kg): "))
altura = float(input("digite sua altura(em m): "))

imc = calc_imc(peso,altura)
print (f"Seu IMC é: {imc}")

if imc < 19.1:
   print("voce esta abaixo do peso.")
elif imc >= 19.1 and imc <= 25.8: 
   print("voce esta com peso normal.")
elif imc >=25.8 and imc <= 27.3:
   print("Pouco acima do Peso")
elif imc >=27.4 and imc <= 32.3:
   print("Voce esta acima do Peso")
elif imc >= 32.4:
   print("Obesidade.")