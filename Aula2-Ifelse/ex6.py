user = "bentoMartins"
senha = "bento123"

user_escrita = input("Digite o user: ")
senha_escrita = input("Digite a senha: ")

if user_escrita == user and senha_escrita == senha:
    print("Login realizado com sucesso!")
else:
    print("Acesso negado! user ou senha incorretos")