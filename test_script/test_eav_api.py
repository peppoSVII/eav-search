import requests
from bs4 import BeautifulSoup


url = "https://orariotreni.eavsrl.it/teleindicatori/ws_getData.php"
data = {
    "device": "M01T1M",
    "tipoLista": "A",
    "codLoc": "1",
    "visualizzazione": "web"
}

response = requests.post(url, data=data)


if response.status_code == 200:
    data = response.text 
    print(data) 
    soup = BeautifulSoup(data, 'html.parser')

    # Estrazione delle righe dei treni
    train_rows = soup.find_all('tr', class_='testoGiallo')

    # Estrazione dati per ogni treno
    trains = []
    for row in train_rows:
        num_treno = row.find('td', class_='numTreno').text.strip()
        categoria = row.find('td', class_='categoria').text.strip()
        destinazione = row.find('div', class_='destinazione').text.strip()
        informazioni = row.find('td', class_='informazioni').text.strip()
        binario = row.find('td', class_='binario').text.strip()
        orario = row.find('td', class_='orario').text.strip()
        ritardo = row.find('td', class_='ritardo').text.strip()

        # Aggiungi le informazioni del treno alla lista
        trains.append({
            "Numero Treno": num_treno,
            "Categoria": categoria,
            "Destinazione": destinazione,
            "Informazioni": informazioni,
            "Binario": binario,
            "Orario": orario,
            "Ritardo": ritardo
        })

    # Stampa o elabora i dati dei treni
    for train in trains:
        print(train)
    
else:
    print(f"Errore nella richiesta: {response.status_code}")