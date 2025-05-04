# 1. Print simples
print("There is something at work in my soul, which I do not understand.")
print("Hello World")
print("Hello Gui")

# 2. Variáveis e reatribuição
meal = "An english muffin"
print("Breakfast:", meal)

meal = "Pizza"
print("Lunch:", meal)

meal = "Burger"
print("Dinner:", meal)

# 3. Tipos de dados
release_year = 2026     # int
runtime = 120           # int
rating_out_of_10 = 9.9  # float

# 4. Operações matemáticas
print(573 - 74 + 1)
print(25 * 2)
print(10 / 2)
print(25 * 68 + 13 / 28)

# 5. Variáveis em expressões
coffee_price = 2.00
number_of_coffees = 4
print("Total coffee cost:", coffee_price * number_of_coffees)

# 6. Área e potências
quilt_width = 8
quilt_length = 8
print("Quilt area:", quilt_width * quilt_length)

print(6 ** 2)      # 6²
print(7 ** 2)      # 7²
print(8 ** 2)      # 8²
print(6 ** 4)      # 6⁴
print(2 ** 10)     # 1024
print(9 ** 3)      # 9³
print(4 ** 0.5)    # Raiz quadrada de 4

#7. Módulo - resto da divisão
print("269 % 10 =", 269 % 10)
print("270 % 10 =", 270 % 10)

# 8. Concatenação de strings
greeting = "Hey there!"
question = "How are you doing?"
print(greeting + " " + question)

# 9. Concatenação com número
age = 10
print("I am " + str(age) + " years old today!")
print("I am", age, "years old today!")  # Alternativa sem str()

#10. Texto longo concatenado
message = (
    "The wind, "
    "which had hitherto carried us along with amazing rapidity, "
    "sank at sunset to a light breeze; "
    "the soft air just ruffled the water and "
    "caused a pleasant motion among the trees as we approached the shore, "
    "from which it wafted the most delightful scent of flowers and hay."
)
print(message)

# 11. Atualização com +=
miles_hiked = 12
miles_hiked += 2
print("Total miles hiked:", miles_hiked)

caption = "What an amazing time to walk through nature!"
caption += " #nofilter"
caption += " #blessed"
print(caption)

#12. Soma acumulada
total_price = 0
total_price += 50.00  # new sneakers
total_price += 39.00  # nice sweater
total_price += 20.00  # fun books
print("Total price:", total_price)

# 13. Strings multilinha
to_you = """
Stranger, if you passing meet me and desire to speak to me, why
  should you not speak to me?
And why should I not speak to you?
"""
print(to_you)

# 14. Exemplo final
my_age = 27
half_my_age = my_age / 2
name = "Guilherme"
print("Hello", name + ", I am", my_age, "years old. Half my age is", half_my_age)
