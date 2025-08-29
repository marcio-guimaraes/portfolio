import requests
from bs4 import BeautifulSoup
import time

URL = "https://sigaa.unb.br/sigaa/public/turmas/listar.jsf"
VALOR_ANTERIOR = None

while True:
    try:
        resp = requests.get(URL)
        soup = BeautifulSoup(resp.text, "html.parser")

        # Pegando todas as linhas com classe 'linhaImpar'
        linhas = soup.find_all("tr", class_="linhaImpar")

        # Supondo que a turma que você quer é a primeira linha
        linha = linhas[0]

        # Pegando a 6ª coluna (índice 5)
        td = linha.find_all("td")[5]
        valor = td.get_text(strip=True)

        if VALOR_ANTERIOR is not None and valor != VALOR_ANTERIOR:
            print(f"Valor mudou! Era {VALOR_ANTERIOR}, agora é {valor}")
            # aqui você pode mandar Telegram, som, notificação etc.

        VALOR_ANTERIOR = valor

    except Exception as e:
        print("Erro:", e)

    time.sleep(60)  # verifica a cada 60 segundos
