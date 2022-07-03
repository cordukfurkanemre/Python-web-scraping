from bs4 import BeautifulSoup
import requests
import re

URL="https://www.amazon.com/dp/B09H4RCTN6"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)
soup1 = BeautifulSoup(page.content, "html.parser")
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")


title = soup2.find(id='productTitle')

rating = soup2.find(id='acrCustomerReviewText')
rating1 = (rating.get_text(strip=True))
rating2 = re.sub('\D','',rating1)

price = soup2.find('span',"a-offscreen")
price1 = (price.get_text(strip=True))
price2 = re.sub('[$(,)]','',price1)

#stock = soup2.find('span','a-size-medium a-color-success')
#stock2 = (stock.get_text(strip=True))
#stock3 = re.sub('[-Only left in stock order soon(In Stock.)]','',stock2)




print(title.get_text(strip=True))
print(rating2)
print(price2)
#print(stock3)