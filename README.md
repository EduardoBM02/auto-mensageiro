# 📬 Auto Mensageiro

Um projeto em Python para envio automatizado de mensagens via **WhatsApp Web** ou **e-mail**, com suporte a mensagens personalizadas ou em massa, e envio de imagens e arquivos.

---

## ✅ Funcionalidades

* Envio de mensagens individuais (WhatsApp e e-mail)
* Envio da mesma mensagem/imagem/arquivo para todos os contatos
* Suporte ao envio de:

  * Texto
  * Imagens (.jpg, .png)
  * Arquivos (.pdf, .docx, .xlsx...)
* Interface de linha de comando (CLI)
* Leitura de contatos a partir de um arquivo `.csv`

---

## 📁 Estrutura do Projeto

```
auto_mensageiro/
├── main.py               # Interface CLI
├── config.py             # Dados de login (NÃO subir para o GitHub)
├── requirements.txt      # Dependências do projeto
├── README.md             # Instruções e documentação
├── .gitignore            
├── data/
│   └── contatos.csv      # Arquivo de exemplo com os contatos
└── utils/
    ├── whatsapp_sender.py
    ├── email_sender.py
    └── formatadores.py
```

---

## ⚙️ Requisitos Básicos

* Python 3.8 ou superior
* Google Chrome ou Microsoft Edge instalado
* Conta de e-mail com acesso a senha de aplicativo (Gmail, por exemplo)

---

## 🧪 Instalação

1. Clone este repositório:

```bash
git clone https://github.com/EduardoBM02/auto_mensageiro.git
cd auto_mensageiro
```

2. Crie um ambiente virtual e ative:

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## 🛠️ Configuração

No arquivo `config.py`, adicione seus dados de e-mail:

```python
EMAIL_USER = "seu_email@email.com"
EMAIL_PASSWORD = "sua_senha_app"
```

> ⚠️ **Importante:** Use uma senha de aplicativo (como a gerada pelo Gmail) para autenticação.

Esse arquivo já está no `.gitignore`, então não será enviado ao GitHub.

---

## 🗂️ Formato do arquivo CSV (individual)

Arquivo: `data/contatos.csv`

```csv
nome,numero,email,mensagem,imagem,anexos
João Silva,+5581999999999,joao@email.com,"Olá João!",caminho/imagem1.jpg,caminho/arquivo.pdf
Maria Souza,81888888888,maria@email.com,"Bom dia!",caminho/imagem2.jpg,"caminho/arquivo2.docx;caminho/arquivo3.xlsx"
Lucas Costa,55 (81) 97777-7777,lucas@email.com,"Segue os documentos solicitados.",imgs/lucas.png,
```

> As colunas **mensagem** e **imagem** podem ou não estar entre aspas. Separe múltiplos arquivos com `;`.

---

## ▶️ Como Usar

No terminal, execute:

```bash
python main.py
```

Você verá um menu como este:

```
=== Auto Mensageiro ===
1. Enviar via WhatsApp
2. Enviar via E-mail
3. Limpar a tela
4. Sair
```

Após isso, poderá escolher entre:

```
1. Enviar mensagens individuais (CSV)
2. Enviar mesma mensagem/imagem para todos
```

---

## 🤝 Contribuições

Contribuições são bem-vindas! Abra uma issue ou envie um pull request 😄

---

## 🛡️ Licença

Este projeto está licenciado sob a Licença MIT.
