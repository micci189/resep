from urllib.request import urlopen
from bs4 import BeautifulSoup

import pandas as pd

def scrap_head(pages:int):
    '''Scrapping nama menu dan link di halaman awal'''
    link = []
    judul = []

    # print(judul_raw)
    # print(len(judul_raw))
    # for page in range(1,251):
    for page in range(1,pages):
        website = f'https://resepmamiku.com/masakan/page/{page}'
        html = urlopen(website)
        data = BeautifulSoup(html, 'html.parser')

        judul_raw = data.findAll("h2", {"class":"entry-title"})
        for i in range(len(judul_raw)):
            for row in judul_raw[i].findAll('a'):
                link.append(row.get('href'))
                judul.append(row.get_text())
                # print(row.get('href'))
                # print(row.get_text())

    data_awal = pd.DataFrame(
        {'judul': judul,
        'link': link
        })

    data_awal.to_csv("data\data_awal.csv")  