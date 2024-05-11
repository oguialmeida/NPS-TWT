# SocialMediaAPIClient NPS Integration

### Introdução
- O SocialMediaAPIClient é uma classe Python que oferece uma interface para interagir com a API de uma plataforma de mídia social. Ele simplifica o processo de enviar solicitações HTTP para a API, lidando com a autenticação e fornecendo métodos convenientes para realizar operações comuns, como enviar mensagens, publicar conteúdo e obter informações de usuário.

### Instalação
Para usar o SocialMediaAPIClient, você precisa instalar a biblioteca requests que é utilizada para fazer requisições HTTP e pode ser facilmente instalada via pip:

```bash
 pip install requests
```

### Login
- login_email_username(username, password): Realiza o login com um nome de usuário ou email e senha.
- login_2fa(login_data, response): Completa a autenticação de dois fatores (se necessário) com os dados de login e a resposta do usuário.

### Publicação de Conteúdo
- create_post(post_text, attachment_url=None, in_reply_to_post_id=None, media_id=None): Cria uma nova publicação com o texto especificado, opcionalmente incluindo anexos, resposta a uma publicação existente ou mídia.

### Interações Sociais
- like_post(post_id): Marca uma publicação como curtida.
- unlike_post(post_id): Desfaz a marcação de curtir de uma publicação.
- share_post(post_id): Compartilha uma publicação.
- unshare_post(post_id): Remove uma publicação compartilhada.

### Gerenciamento de Mensagens
- get_message_conversations(cursor=None): Obtém conversas de mensagens.
- get_message_conversation(username=None, user_id=None, cursor=None): Obtém uma conversa de mensagem com um usuário específico.
- send_message(message, to_user_name=None, to_user_id=None, media_id=None): Envia uma mensagem para um usuário.


## Authors

- [@Guilherme Gomes](https://www.github.com/oguialmeida)

- [@Marcos Vinicius](https://www.github.com/TgdAnubis)

- [@Pedro Wilson](https://www.github.com)
