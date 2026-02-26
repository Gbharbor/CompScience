# regras
# -A senha deve ter no minimo 8 caracteres
# -a senha n pode ser 12345678
# -o resultado esperado e dizer se a senha e valida ou nao 

password = input("Digite uma senha: ")

if len(password) >= 8 and password != "12345678":
    print("Senha válida.")

elif len(password) < 8:
    print("Senha inválida. Deve ter pelo menos 8 caracteres.")

elif password == "12345678":
    print("Senha inválida. Sequência não permitida.")