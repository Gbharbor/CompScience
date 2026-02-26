password = input("Digite uma senha: ")

# Contar caracteres
char_count = len(password)

# Verificar se é sequência proibida
is_sequence = password == "12345678"

if char_count < 8:
    print("Senha inválida. Deve ter pelo menos 8 caracteres.")

elif is_sequence:
    print("Senha inválida. Não pode ser uma sequência simples.")

else:
    print("Senha válida. Muito bem.")