from bs4 import BeautifulSoup
import requests

data = requests.get('https://www.imdb.com/find?s=ep&q=thriller&ref_=nv_sr_sm')
soup = BeautifulSoup(data.content, 'html.parser')
movieTable = soup.find('table', {'class': 'findList'})
rows = movieTable.findAll('tr')
for row in rows:
    rowdata = row.findAll('td')
    name = rowdata[1].a.text
    suburl = rowdata[1].a['href']
    subdata = requests.get('https://www.imdb.com'+suburl)
    childSoup = BeautifulSoup(subdata.content, 'html.parser')
    genres = childSoup.find('ul', {'class': 'ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content base'})
    li = genres.findAll('li')
    genre = []
    for item in li:
        genreText = item.a.text
        if "Horror" in genreText:
            genre.append(genreText)
            print("{}{}{}".format(name, ' --- ', genre[0]))




