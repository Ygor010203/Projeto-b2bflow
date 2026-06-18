# Automação de Mensagens WhatsApp

Este projeto é uma ferramenta de automação desenvolvida em Python que lê contatos armazenados em uma tabela do **Supabase** e realiza o disparo automático de mensagens personalizadas via **Z-API**.

 🚀 Funcionalidades
- Leitura dinâmica de contatos (nome e número) do banco de dados Supabase.
- Disparo de mensagens personalizadas ("Olá, <nome>, tudo bem?") para cada contato.
- Tratamento de erros e feedback em tempo real no terminal.

 🛠 Tecnologias Utilizadas
 Python: Linguagem principal.
Supabase: Banco de dados para armazenamento dos contatos.
Z-API: API para integração e envio de mensagens via WhatsApp.

🛠 Configure as variáveis de ambiente
Por questões de segurança, as credenciais não estão incluídas.

Crie um arquivo chamado .env na raiz do projeto.

Preencha com os dados seguindo o modelo abaixo:

Plaintext
SUPABASE_URL=sua_url_do_supabase
SUPABASE_KEY=sua_key_do_supabase
ZAPI_URL=sua_url_da_zapi
ZAPI_TOKEN=seu_token_da_zapi

 ⚙️Como rodar o projeto

Clone este repositório:
git clone [https://github.com/Ygor010203/Projeto-b2bflow.git](https://github.com/Ygor010203/Projeto-b2bflow.git)
