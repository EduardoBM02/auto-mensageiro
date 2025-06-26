import csv
import os
from utils.formatadores import formatar_numero, formatar_caminho_imagem
from utils.whatsapp_sender import enviar_whatsapp
from utils.email_sender import enviar_email

def carregar_contatos():
    contatos = []
    with open("data/contatos.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for linha in reader:
            contatos.append({
                "nome": linha["nome"].strip(),
                "numero": linha["numero"].strip(),
                "email": linha["email"].strip(),
                "mensagem": linha.get("mensagem", "").strip(),
                "imagem": linha.get("imagem", "").strip(),
                "anexos": linha.get("anexos", "").strip()
            })
    return contatos

def menu():
    contatos = carregar_contatos()

    while True:
        print("\n=== Auto Mensageiro ===")
        print("1. Enviar via WhatsApp")
        print("2. Enviar via E-mail")
        print("3. Limpar a tela")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha not in ["1", "2", "3", "4"]:
            os.system("cls" if os.name == "nt" else "clear")
            print("Opção inválida.")
            continue
        if escolha == "4":
            print("Saindo...")
            break
        elif escolha == "3":
            os.system("cls" if os.name == "nt" else "clear")
            continue

        print("\n1. Enviar mensagens individuais (CSV)")
        print("2. Enviar mesma mensagem/imagem/anexos para todos")
        tipo_envio = input("Escolha o tipo de envio: ")

        if tipo_envio not in ["1", "2"]:
            print("Opção inválida.")
            continue

        mensagem, imagem, anexos = "", None, ""

        if tipo_envio == "2":
            mensagem = input("Digite a mensagem: ").strip()
            imagem_input = input("Caminho da imagem (opcional): ").strip()
            imagem = formatar_caminho_imagem(imagem_input or None)
            if escolha == "2":
                anexos = input("Caminhos dos anexos (opcional, separados por ';'): ").strip()

        for contato in contatos:
            try:
                nome = contato["nome"]
                numero = formatar_numero(contato["numero"])
                email = contato["email"]

                msg = mensagem if tipo_envio == "2" else contato["mensagem"]
                img = imagem if tipo_envio == "2" else formatar_caminho_imagem(contato["imagem"] or "")
                files = anexos if tipo_envio == "2" else contato.get("anexos", "")

                if escolha == "1":  # WhatsApp
                    enviar_whatsapp(numero, mensagem=msg, caminho_imagem=img)

                elif escolha == "2":  # E-mail
                    assunto = "Mensagem Automática"
                    enviar_email(email, assunto, msg, caminho_imagem=img, anexos=files)

            except Exception as e:
                print(f"Erro com {contato['nome']}: {e}")

if __name__ == "__main__":
    menu()
