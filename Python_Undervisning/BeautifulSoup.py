import urllib.request
from bs4 import BeautifulSoup
import ssl
import json


ssl._create_default_https_context = ssl._create_unverified_context

url = "https://politiken.dk/"
request = urllib.request.Request(url)
html = urllib.request.urlopen(request).read()
soup = BeautifulSoup(html,'html.parser')

main_table = soup.find("section",attrs={'class':'frontpage__section'})

links = main_table.find_all("a")

print(links)


# Advanced scraper (2)


records = []

for link in links:
    title = link.text
    url = link[ "href"]

    new_record = {
        'title': title,
        'url': url
        }

    records.append(new_record)

#print(json.dumps(records))

f = open("politiken.txt", "w")

f.write(json.dumps(records))