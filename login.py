import requests

# URL da página de login
login_url = 'https://webdivulgacao.luzdosaber.com.br/Login.aspx?Pagina=default.aspx'

# Credenciais de login
payload = {
    'username': '',
    'password': ''
}

# Iniciar uma sessão
with requests.Session() as session:
    # Enviar uma requisição POST com as credenciais
    response = session.post(login_url, data=payload)

    # Verificar se o login foi bem-sucedido (opcional)
    if response.status_code == 200:
        print("Login bem-sucedido!")

        # Agora você pode acessar outras páginas que exigem autenticação
        dashboard_url = 'https://webdivulgacao.luzdosaber.com.br/default.aspx'
        dashboard_response = session.get(dashboard_url)

        # Exibir o conteúdo da página protegida
        print(dashboard_response.text)
    else:
        print("Falha no login.")
