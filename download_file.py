import requests

index = 0

for surah in range(114):
    index += 1

    url = "http://api.alquran.cloud/v1/surah/" +str(index)+ "/en.hilali"
    r = requests.get(url, allow_redirects=True)
    outFileName="/Users/adrian/Desktop/quran_translate_english/quran_translate_" +str(index)+ ".json"
    print("Surah number " +str(index)+ " downloaded!")
    f= open(outFileName,"wb")
    f.write(r.content)
    f.close()
