import re
import os

def formatar_numero(numero_raw):
    """Formata número de telefone adicionando o código do país +55, se necessário."""

    numero = re.sub(r'\D', '', numero_raw)

    if len(numero) == 11 and numero.startswith(('1', '2', '3', '4', '5', '6', '7', '8', '9')):
        return f"+55{numero}"
    elif len(numero) == 10:
        return f"+559{numero}"
    elif len(numero) == 13 and numero.startswith("55"):
        return f"+{numero}"
    elif len(numero) == 14 and numero.startswith("+55"):
        return numero
    else:
        raise ValueError(f"Número de telefone inválido: {numero_raw}")
    
def formatar_caminho_imagem(caminho_raw):
    """Remove aspas e espaços, e converte para caminho absoluto se possível."""
    if not caminho_raw:
        return None

    caminho = caminho_raw.strip().strip('"').strip("'")

    if not caminho:
        return None

    caminho_absoluto = os.path.abspath(caminho)
    return caminho_absoluto if os.path.exists(caminho_absoluto) else caminho
    