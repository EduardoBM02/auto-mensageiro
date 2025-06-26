# 📬 Auto Mensageiro

Um projeto simples em Python para envio automatizado de mensagens via **WhatsApp Web** e **e-mail** usando uma planilha CSV de contatos.

---

## 🔧 Funcionalidades

- Envio de mensagens de texto pelo WhatsApp Web.
- Envio de imagens com ou sem legenda pelo WhatsApp.
- Envio de e-mails com texto, imagens ou arquivos (Excel, PDF, Word).
- Suporte a mensagens individuais ou padrão para todos os contatos.
- Interface de linha de comando simples e intuitiva (CLI).
- Formatação automática de números de telefone e caminhos de arquivos.

---

## 📁 Estrutura

auto_mensageiro/
│
├── main.py # Interface CLI
├── config.py # Dados de login (NÃO subir para o GitHub)
├── requirements.txt # Dependências do projeto
├── README.md
│
├── data/
│ └── contatos.csv # Arquivo de exemplo com os contatos
│
└── utils/
├── whatsapp_sender.py
├── email_sender.py
└── formatadores.py

---

## 📄 Exemplo de CSV (`data/contatos.csv`)

```csv
nome,numero,email,mensagem,imagem,arquivos
João Silva,+5581987654321,joao@gmail.com,Olá João!,imagens/joao.png,
Maria Souza,+5581998765432,maria@gmail.com,Boa tarde!,imagens/maria.jpg,documentos/relatorio.pdf;documentos/dados.xlsx
