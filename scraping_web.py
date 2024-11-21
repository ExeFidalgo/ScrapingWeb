import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrapear_lenguajes():
    try:
        # Scraping de la página TIOBE
        # URL de la página de TIOBE
        url_tiobe = "https://www.tiobe.com/tiobe-index/"
        # Realiza una solicitud HTTP para obtener el contenido de la página
        respuesta_tiobe = requests.get(url_tiobe)
        # Crea un objeto BeautifulSoup para analizar el HTML de la página
        sopa_tiobe = BeautifulSoup(respuesta_tiobe.text, 'html.parser')
        
        # Selecciona la tabla con el ID "top20"
        tabla_tiobe = sopa_tiobe.select_one('table#top20')
        # Selecciona todas las filas de la tabla, omitiendo la cabecera
        filas_tiobe = tabla_tiobe.select('tr')[1:]
        
        # Lista para almacenar los datos extraídos
        datos_tiobe = []
        for fila in filas_tiobe:
            # Selecciona todas las celdas de la fila
            celdas = fila.select('td')
            # Verifica si hay al menos 6 columnas
            if len(celdas) >= 6:
                # Extrae los datos relevantes y los agrega a la lista
                datos_tiobe.append({
                    "Posición": celdas[0].text.strip(),
                    "Lenguaje": celdas[4].text.strip(),
                    "Porcentaje": celdas[5].text.strip()
                })

        # Scraping de la página Tecsify
        # URL de la página de Tecsify
        url_tecsify = "https://tecsify.com/blog/top-lenguajes-2024/"
        # Realiza una solicitud HTTP para obtener el contenido de la página
        respuesta_tecsify = requests.get(url_tecsify)
        # Crea un objeto BeautifulSoup para analizar el HTML de la página
        sopa_tecsify = BeautifulSoup(respuesta_tecsify.text, 'html.parser')
        
        # Selecciona la tabla que se encuentra dentro del artículo
        tabla_tecsify = sopa_tecsify.select_one('article table')
        # Selecciona todas las filas de la tabla, omitiendo la cabecera
        filas_tecsify = tabla_tecsify.select('tr')[1:]
        
        # Lista para almacenar los datos extraídos
        datos_tecsify = []
        for fila in filas_tecsify:
            # Selecciona todas las celdas de la fila
            celdas = fila.select('td')
            # Verifica si hay al menos 6 columnas
            if len(celdas) >= 6:
                # Extrae los datos relevantes y los agrega a la lista
                datos_tecsify.append({
                    "Posición": celdas[0].text.strip(),
                    "Lenguaje": celdas[4].text.strip(),
                    "Porcentaje": celdas[5].text.strip()
                })

        # Scraping de la página StaticTimes
        # URL de la página de StaticTimes
        url_static_times = "https://statisticstimes.com/tech/top-computer-languages.php"
        # Realiza una solicitud HTTP para obtener el contenido de la página
        respuesta_static_times = requests.get(url_static_times)
        # Crea un objeto BeautifulSoup para analizar el HTML de la página
        sopa_static_times = BeautifulSoup(respuesta_static_times.text, 'html.parser')
        
        # Selecciona la tabla con el ID "table_id1" y su cuerpo
        tabla_static_times = sopa_static_times.select_one('#table_id1 tbody')
        # Selecciona todas las filas del cuerpo de la tabla
        filas_static_times = tabla_static_times.select('tr')
        
        # Lista para almacenar los datos extraídos
        datos_static_times = []
        for fila in filas_static_times:
            # Selecciona todas las celdas de la fila
            celdas = fila.select('td')
            # Verifica si hay al menos 5 columnas
            if len(celdas) >= 5:
                # Extrae los datos relevantes y los agrega a la lista
                datos_static_times.append({
                    "Posición": celdas[0].text.strip(),
                    "Lenguaje": celdas[2].text.strip(),
                    "Porcentaje": celdas[3].text.strip(),
                    "Tendencia": celdas[4].text.strip()
                })

        # Crear un archivo Excel con hojas separadas para cada fuente de datos
        with pd.ExcelWriter('ranking_lenguajes.xlsx') as escritor:
            # Guardar los datos de TIOBE en una hoja llamada "TIOBE"
            pd.DataFrame(datos_tiobe).to_excel(escritor, sheet_name='TIOBE', index=False)
            # Guardar los datos de Tecsify en una hoja llamada "Tecsify"
            pd.DataFrame(datos_tecsify).to_excel(escritor, sheet_name='Tecsify', index=False)
            # Guardar los datos de StaticTimes en una hoja llamada "StaticTimes"
            pd.DataFrame(datos_static_times).to_excel(escritor, sheet_name='StaticTimes', index=False)
        
        # Mensaje de éxito
        print("Archivo Excel creado exitosamente")

    except Exception as e:
        # Mensaje de error en caso de que ocurra un problema
        print("Ocurrió un error durante el scraping:", str(e))

# Llama a la función para ejecutar el scraping
scrapear_lenguajes()
