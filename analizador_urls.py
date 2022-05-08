import json
import requests
import time
from openpyxl import Workbook


def Virus_Total():
    t = 1
    m = 2
    api = 'ea7157997551a5e361931857b8e5e7ab4a7ad7b9d56ad7256390345d02ef96b1'
    urls = open("urls_sospechosas.txt", "r")
    excel = Workbook()
    hc = excel.active
    hc['A1'] = 'URL'
    hc['B1'] = 'FECHA DE ANALISIS'
    hc['C1'] = 'TOTAL DE ANALISIS'
    hc['D1'] = 'ANALISIS POSITIVOS'
    hc['E1'] = 'CLASIFICACION'
    for x in urls:
        if t == 5:
            time.sleep(62.00)
            api_url = 'https://www.virustotal.com/vtapi/v2/url/report'
            params = dict(apikey = api, resource = x, scan = 0)
            response = requests.get(api_url, params=params)
            if response.status_code == 200:
                result = response.json()
                print(json.dumps(result, sort_keys=False, indent=4))
                hc['A' + str(m)] = str(x)
                hc['B' + str(m)] = result['scan_date']
                hc['C' + str(m)] = result['total']
                hc['D' + str(m)] = result['positives']
                if result['positives'] <= 3:
                    hc['E' + str(m)] = 'Baja'
                elif result['positives'] > 3 and result['positives'] <= 10:
                    hc['E' + str(m)] = 'Medio'
                elif result['positives'] > 10:
                    hc['E' + str(m)] = 'Alto'
        else:
            api_url = 'https://www.virustotal.com/vtapi/v2/url/report'
            params = dict(apikey = api, resource = x, scan = 0)
            response = requests.get(api_url, params=params)
            if response.status_code == 200:
                result = response.json()
                print(json.dumps(result, sort_keys=False, indent=4))
                hc['A' + str(m)] = str(x)
                hc['B' + str(m)] = result['scan_date']
                hc['C' + str(m)] = result['total']
                hc['D' + str(m)] = result['positives']
                if result['positives'] <= 3:
                    hc['E' + str(m)] = 'Baja'
                elif result['positives'] > 3 and result['positives'] <= 10:
                    hc['E' + str(m)] = 'Medio'
                elif result['positives'] > 10:
                    hc['E' + str(m)] = 'Alto'
        m = m + 1
        t = t + 1
    #Guarda un excel con la informacion anterior
    excel.save('reporte_analizador_urls.csv')
    #Cierra el objeto que estabamos utilizando
    urls.close()
