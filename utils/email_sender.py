import yagmail
from config import EMAIL_USER, EMAIL_PASSWORD

def enviar_email(destinatario, assunto, corpo_texto, caminho_imagem=None, anexos=None):
    try:
        yag = yagmail.SMTP(EMAIL_USER, EMAIL_PASSWORD)
        conteudo = [corpo_texto]

        if caminho_imagem:
            conteudo.append(caminho_imagem)

        # Lida com múltiplos anexos (espera uma lista)
        if anexos:
            if isinstance(anexos, str):
                anexos = [a.strip() for a in anexos.split(";") if a.strip()]
            conteudo.extend(anexos)

        yag.send(to=destinatario, subject=assunto, contents=conteudo)
        print(f"E-mail enviado para {destinatario}")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

