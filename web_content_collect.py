import requests
from bs4 import BeautifulSoup

link1 = "https://litequran.net/"

html1 = requests.get(link1).text
soup1 = BeautifulSoup(html1, "html.parser")

index = 0

for url in soup1.find("ol", {"class":"list"}).find_all('a', href=True):
    print(url['href'])

    index += 1

    link2 = url['href']
    html2 = requests.get(link2).text
    soup2 = BeautifulSoup(html2, "html.parser")
    res = soup2.find_all("article", {"class": "surat"})
    outFileName="/Users/adrian/Desktop/quran_latin/quran_latin_" +str(index)+".json"
    f= open(outFileName,"w+")
    f.write("{\"data\":")
    f.write("{\"ayahs\":[")
    for text in res:
        data = text.find_all("span", {'class': 'bacaan'})
        for item in data:
            aData = item.text
            if data.index(item) == len(data)-1:
                f.write("{\"text\":\"" +aData+ "\"}")
            else:
                f.write("{\"text\":\"" +aData+ "\"},")

    f.write("]")
    f.write("}")
    f.write("}")
    f.close()
