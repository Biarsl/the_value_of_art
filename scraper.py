from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import os
import pandas as pd
from urllib.parse import urljoin

# Configurações do Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")  # Executa sem abrir janela
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service()  # Use Service(path_to_chromedriver) se necessário
driver = webdriver.Chrome(service=service, options=chrome_options)

# Cria pasta para imagens
os.makedirs('saatchi_art_images', exist_ok=True)

base_url = "https://www.saatchiart.com"
url = f"{base_url}/paintings"
headers = {'User-Agent': 'Mozilla/5.0'}

data = []
max_pages = 40  # Ajustar se quiser mais
delay = 10

def download_image(image_url, filename):
    try:
        response = requests.get(image_url, headers=headers, stream=True)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            return True
    except Exception as e:
        print(f"[ERRO] Falha ao baixar imagem {image_url}: {e}")
    return False

for page in range(1, max_pages + 1):

    print(f"\n[INFO] Processando página {page}")

    try:
        driver.get(f"{url}?page={page}")

        # Espera até pelo menos uma imagem aparecer
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'img'))
        )

        # 🔽 Salvar HTML da página atual
        with open(f"page_{page}.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Pega o seletor mais amplo de cada imagem
        cards = soup.select ('.Polaroid_polaroidContainer__dH4_G')

        print(f"[INFO] {len(cards)} obras encontradas")

        for i, card in enumerate(cards, start=1):
            try:

                # Imagem
                img_tag = card.select_one('img')
                image_url = img_tag['src'] if img_tag else 'N/A'

                # Artista e tipo de arte (retirado do "alt" da imagem)
                image_alt = img_tag['alt'] if img_tag else 'N/A'
                partes = image_alt.split(" by ")
                type_alt = partes[0]
                type = type_alt if type_alt else "tipo não encontrado"
                artista_alt = partes[1]
                artista = artista_alt if artista_alt else "artista não encontrado"

                # Título da pintura (retirado do "a")
                title_tag = card.select_one('a')['title']
                titulo = title_tag if title_tag else "título não encontrado"
                print(titulo)

                # Procura um <a> que tenha o atributo alt (mais robusto que usar classe)
                link_tag = card.select_one('a[alt]')
                titulo = link_tag['alt'].strip() if link_tag and 'alt' in link_tag.attrs else "título não encontrado"


                # Tamanho da pintura
                size_tag = card.select_one('span[data-type="dimensions-unit"]')
                size = size_tag.get_text(strip=True) if size_tag else "tamanho não encontrado"
                print(size)

                # Material e preço
                tipo_da_pintura_tag = card.select_one('.Polaroid_textGunmetalOpacity__l32Dl').get_text(strip=True)
                tipo_da_pintura = tipo_da_pintura_tag if tipo_da_pintura_tag else "tipo da pintura não encontrado"

                price_tag = card.select_one('.Polaroid_polaroidPriceAndActionsPrice__oUNRP').get_text(strip=True)
                price = price_tag if price_tag else "preço não encontrado"

                # Nome do arquivo da imagem (usando o title)
                image_filename = os.path.join("saatchi_art_images", f"page{page}_img{i}.jpg")


                downloaded = download_image(image_url, image_filename) if image_url != 'N/A' else False


                # Montagem do CSV
                data.append({
                    'Título': titulo,
                    'Artista': artista,
                    'Preço': price,
                    'Tamanho': size,
                    'Painting style': tipo_da_pintura, # Material
                    'Painting type': type_alt,
                    'Image_URL': image_url,
                    'Image_Downloaded': downloaded,
                    'Image_Path': image_filename if downloaded else 'imagem não encontrada',

                })

            except Exception as e:
                print(f"[ERRO] Problema ao processar obra: {e}")
                continue

    except Exception as e:
        print(f"[ERRO] Falha ao carregar página {page}: {e}")
        continue

    time.sleep(delay)

# Salva CSV
df = pd.DataFrame(data)
df.to_csv('saatchi_art_data.csv', index=False)
print(f"\n✅ Coleta concluída: {len(data)} obras")
print("📁 Arquivo CSV salvo como 'saatchi_art_data.csv'")
print("🖼️ Imagens salvas em 'saatchi_art_images/'")
