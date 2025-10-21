print("** MINI SISTEMA DE USUÁRIO **\n")

def cadastro_new_user():
    print("CADASTRO DE NOVOS USUÁRIOS: \n")
    new_username = input("Digite seu username: ")
    new_password = input("Digite sua nova senha: ")
    nova_senha = new_password
    new_password = input("Confirme sua senha: ")
    while new_password != nova_senha:
        new_password = input("Tente novamente! Digite sua nova senha: ")
    print("Olá, ", new_username, ". Você foi cadastrado!")

opcao_inicial = int(input("Digite 1 para fazer LOGIN ou Digite 2 para CADASTRO: \n"))
if opcao_inicial == 1 or opcao_inicial == 2:
    if opcao_inicial == 1:
        username_cad = input("Digite seu usuário cadastrado: ")
        password_cad = input("Digite sua senha cadastrada: ")
        print("Usuário Logado no MINI SYSTEM")
    else:
        cadastro_new_user()
else:
    print("Opção não encontrada! Tente novamente mais tarde.")



