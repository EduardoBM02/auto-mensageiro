import pywhatkit
from datetime import datetime, timedelta
import os
import time

def enviar_whatsapp(numero, mensagem=None, caminho_imagem=None, primeira_vez=False):
    """
    Envia uma mensagem de texto ou imagem via WhatsApp Web.
    - Se fornecer apenas mensagem → envia texto.
    - Se fornecer imagem → envia imagem com legenda (se houver mensagem).
    """
    if caminho_imagem:  # Envio de imagem
        if not os.path.exists(caminho_imagem):
            print(f"Imagem não encontrada: {caminho_imagem}")
            return
        print(f"Enviando imagem para {numero} com legenda: {mensagem or '[sem legenda]'}")
        pywhatkit.sendwhats_image(
            receiver=numero,
            img_path=caminho_imagem,
            caption=mensagem or "",
            wait_time=30 if primeira_vez else 15
        )
        # Aguarda o envio concluir antes de continuar com o próximo
        time.sleep(5)  # Ajuste conforme necessário (5~10 segundos geralmente funciona bem)

    elif mensagem:  # Envio de texto
        agora = datetime.now()
        envio = agora + timedelta(minutes=1)
        hora, minuto = envio.hour, envio.minute
        print(f"Agendando mensagem para {numero} às {hora}:{minuto}")
        pywhatkit.sendwhatmsg(numero, mensagem, hora, minuto)

    else:
        print("Erro: Nenhuma mensagem ou imagem fornecida.")
 
