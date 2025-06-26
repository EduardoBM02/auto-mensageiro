##📬 Auto Mensageiro

Um projeto em Python para envio automatizado de mensagens via WhatsApp Web ou e-mail, com suporte a mensagens personalizadas ou em massa, e envio de imagens e arquivos.

---
##✅ Funcionalidades

- Envio de mensagens individuais (WhatsApp e e-mail)
- Envio da mesma mensagem/imagem/arquivo para todos os contatos
- Suporte ao envio de:
- Texto
- Imagens (.jpg, .png)
- Arquivos (.pdf, .docx, .xlsx...)
- Interface de linha de comando (CLI)
- Leitura de contatos a partir de um arquivo .csv
---
##📁 Estrutura do Projeto

<pre><code> 
  auto_mensageiro/ 
  ├── main.py # Interface CLI 
  ├── config.py # Dados de login (NÃO subir para o GitHub) 
  ├── requirements.txt # Dependências do projeto 
  ├── README.md # Instruções e documentação 
  ├── data/ 
  │     └── contatos.csv # Arquivo de exemplo com os contatos 
  └── utils/ 
        ├── whatsapp_sender.py 
        ├── email_sender.py 
        └── formatadores.py</code></pre>
        
---
##⚙️ Requisitos Básicos

- Python 3.8 ou superior
- Google Chrome ou Microsoft Edge instalado
- Conta de e-mail com acesso a senha de aplicativo (Gmail, por exemplo)
---
##🧪 Instalação

- Clone este repositório:
<code>
git clone https://github.com/EduardoBM02/auto_mensageiro.git
cd auto_mensageiro
</code>
- Crie um ambiente virtual e ative:
<code>
python -m venv venv
venv\Scripts\activate  # Windows
</code>
<code>
- Instale as dependências:
</code>
pip install -r requirements.txt

---
#🛠️ Configuração

No arquivo config.py, adicione seus dados de e-mail:
<code>
EMAIL_USER = "seu_email@email.com"
EMAIL_PASSWORD = "sua_senha_app"
</code>

---
##⚠️ Importante: Use uma senha de aplicativo (como a gerada pelo Gmail) para autenticação.

Esse arquivo já está no .gitignore, então não será enviado ao GitHub.

---
##🗂️ Formato do arquivo CSV (individual)

Arquivo: data/contatos.csv
<code>
nome,numero,email,mensagem,imagem
João Silva,+5581999999999,joao@email.com,"Olá João!",caminho/imagem1.jpg
Maria Souza,+5581888888888,maria@email.com,"Bom dia!",caminho/imagem2.jpg;caminho/arquivo.pdf
</code>
As colunas mensagem e imagem podem ou não estar entre aspas. Separe múltiplos arquivos com |.

---
##▶️ Como Usar

No terminal, execute:
<code>
python main.py
</code>
Você verá um menu como este:
<code>
=== Auto Mensageiro ===
1. Enviar via WhatsApp
2. Enviar via E-mail
3. Limpar a tela
4. Sair
</code>
Após isso, poderá escolher entre:

1. Enviar mensagens individuais (CSV)
2. Enviar mesma mensagem/imagem para todos

---
##🤝 Contribuições

Contribuições são bem-vindas! Abra uma issue ou envie um pull request 😄

---
##🛡️ Licença

Este projeto está licenciado sob a Licença MIT.

