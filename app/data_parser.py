from bs4 import BeautifulSoup
import pandas as pd

def parse_train_data(raw_data):
    soup = BeautifulSoup(raw_data, "html.parser")
    train_info = []

    # Find the relevant table rows
    rows = soup.select("table:nth-of-type(2) tr.testoGiallo")
    
    for row in rows:
        cells = row.find_all("td")
        if len(cells) > 0:
            train_info.append({
                "Train Number": cells[0].text.strip(),
                "Category": cells[1].text.strip(),
                "Destination": cells[2].text.strip(),
                "Information": cells[3].text.strip(),
                "Platform": cells[4].text.strip(),
                "Time": cells[5].text.strip(),
                "Delay": cells[6].text.strip(),
            })

    return pd.DataFrame(train_info)
