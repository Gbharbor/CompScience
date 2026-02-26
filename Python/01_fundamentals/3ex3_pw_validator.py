#
# Separa responsabilidade
# Permite reutilização
# Facilita testes automatizados
# Escala para regras mais complexas
# É arquitetura limpa

def validate_password(password: str) -> bool:
    if len(password) < 8:
        return False
    
    if password == "12345678":
        return False

    return True

password = input("Digite uma senha: ")

if validate_password(password):
    print("Senha válida.")
else:
    print("Senha inválida.")