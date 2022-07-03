from bs4 import BeautifulSoup
import requests


URL="https://www.amazon.com/s?k=kitchen+organization"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)
soup1 = BeautifulSoup(page.content, "html.parser")
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

a = 0
while a < 40:
    try:
        products = soup2.find("div",{"class":"s-main-slot s-result-list s-search-results sg-row"})
        ASINs = products.find("div",{"data-index":"{}".format(a)})
        ASIN = ASINs.get("data-asin")
        print(ASIN)
        a +=1
    except:
        a +=1
