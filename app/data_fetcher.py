import requests

def fetch_train_data():
    url = "https://orariotreni.eavsrl.it/teleindicatori/ws_getData.php"
    params = {
        "device": "M01T1M",
        "tipoLista": "A",
        "codLoc": "1",
        "visualizzazione": "mobile"
    }

    try:
        response = requests.post(url, data=params)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
