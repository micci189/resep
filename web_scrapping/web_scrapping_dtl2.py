from urllib.request import urlopen
from bs4 import BeautifulSoup

import pandas as pd


link_list = []
ingredients_list = []
spice_list = []
method_list = []

# data = pd.read_csv("data_awal.csv")
# data.drop("Unnamed: 0", axis=1, inplace=True)

# for link in data['link'][4000:5000]:
# for link in data['link'][start:end]:

website = 'https://resepmamiku.com/ayam-bumbu-kuning-dhiahoddie'
html = urlopen(website)
data = BeautifulSoup(html, 'html.parser')

recipe_content_raw = data.findAll('div', {'class': 'recipe-content'})
recipe_content = recipe_content_raw[0].find_all(['h2','p'])
    
bahan = ''
bumbu = ''
metode = ''

# print(recipe_content)
print(f"\n len recipe_content = {len(recipe_content)}\n")

for i in range(0,len(recipe_content),2):
    # print(str(i) + recipe_content[i].get_text())
    if recipe_content[i].get_text().lower().find('bahan') >= 0 and i+1 < len(recipe_content):
        ingredients_raw = recipe_content[i+1].findAll('label')
        for x in range(len(ingredients_raw)):
            if x == len(ingredients_raw)-1:
                bahan += ingredients_raw[x].get_text()
            else:
                bahan += f'{ingredients_raw[x].get_text()}\n'
    
    elif (recipe_content[i].get_text().lower().find('cara') >= 0 or recipe_content[i].get_text().lower().find('buat') >= 0) and i+1 < len(recipe_content):
        method_raw = recipe_content[i+1].findAll('label')
        print(f"\nmetode_raw = {method_raw}\n")
        for x in range(len(method_raw)):
            if x == len(method_raw)-1:
                metode += method_raw[x].get_text()
            else:
                metode += f'{method_raw[x].get_text()}\n'

    elif recipe_content[i].get_text().lower().find('bumbu') >= 0 and i+1 < len(recipe_content):
        spice_raw = recipe_content[i+1].findAll('label')
        for x in range(len(spice_raw)):
            if x == len(spice_raw)-1:
                bumbu += spice_raw[x].get_text()
            else:
                bumbu += f'{spice_raw[x].get_text()}\n'

# link_list.append(website)
# ingredients_list.append(bahan)
# spice_list.append(bumbu)
# method_list.append(metode)

print(f'bahan : {bahan}\n')
print(f'bumbu : {bumbu}\n')
print(f'metode : {metode}\n')

# data_detail = pd.DataFrame(
#     {
#     'link': link_list,
#     'bahan': ingredients_list,
#     'bumbu': spice_list,
#     'metode': method_list
#     })

# data_detail.to_csv("data\data_detail.csv") # => 0:1000
# data_detail.to_csv("data\data_detail2.csv") # => 1000:2000
# data_detail.to_csv("data\data_detail3.csv") # => 2000:3000
# data_detail.to_csv("data\data_detail4.csv") # => 3000:4000
# data_detail.to_csv("data\data_detail5.csv") # => 4000:5000
# data_detail.to_csv(f"data\{filename}") # => 4000:5000
        





# judul_raw = data.findAll("h2", {"class":"entry-title"})


# # print(judul_raw)
# # print(len(judul_raw))
# for page in range(1,2):
#     website = f'{root}/masakan/page/{page}'
#     html = urlopen(website)
#     data = BeautifulSoup(html, 'html.parser')

#     judul_raw = data.findAll("h2", {"class":"entry-title"})
#     for i in range(len(judul_raw)):
#         for row in judul_raw[i].findAll('a'):
#             link.append(row.get('href'))
#             judul.append(row.get_text())
#             # print(row.get('href'))
#             # print(row.get_text())

# data_awal = pd.DataFrame(
#     {'judul': judul,
#      'link': link
#     })

# data_awal.to_csv("data_awal.csv")