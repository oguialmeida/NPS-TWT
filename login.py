from API import SocialMediaAPIClient
from getpass import getpass

api_key = "sua_chave_rapidapi_aqui"
cliente = SocialMediaAPIClient(api_key)

nome_de_usuario = input("Nome de Usuário/Email: ")
senha = getpass()

resposta = cliente.login_email_username(nome_de_usuario, senha)

if "success" in resposta and resposta["success"] == True:
    print("Sessão: " + resposta["session"])

else:
    if "errors" in resposta:
        print("Erro: " + resposta["errors"][0]["message"])

    elif "login_data" in resposta:
        while True:
            dados_login = resposta["login_data"]
            resp = getpass(resposta["message"] + ": ")

            resposta = cliente.login_2fa(dados_login, resp)

            if "login_data" in resposta:
                pass
            
            elif resposta["success"] == True:
                print("Sessão: " + resposta["session"])
                break

            else:
                print("Erro: " + resposta["error"])
                break

    else:
        print("Erro: Não é possível fazer login.")
