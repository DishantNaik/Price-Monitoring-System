from bs4 import BeautifulSoup
import time
import requests

HEADERS = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}

def amazonScraper(url):
    page = requests.get(url,headers=HEADERS)
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'lxml')
        
        title = soup.find(id = "productTitle").get_text().strip()
        
        price = soup.find(id = "priceblock_ourprice").get_text().strip()
        price = price.split('$')
        price = float(price[1])
        
        print(title)
        print(price)
    else:
        print("Page Not found")

def bestBuyScraper(url):
    page = requests.get(url,headers = HEADERS)
    if page.status_code == 200 :
        soup = BeautifulSoup(page.content,'lxml')

        title = soup.find('h1',{'class':'heading-5 v-fw-regular'}).get_text().strip()
        
        pricetmp = soup.find('div',{'class':'priceView-hero-price priceView-customer-price'})
        price = pricetmp.find('span',{'aria-hidden':'true'}).get_text().strip()
        price = price.split('$')
        price = float(price[1])
        
        print(title)
        print(price)
    else:
        print("Page Not found")

def walmartScraper(url):
    page = requests.get(url, headers = HEADERS)
    if page.status_code == 200:
        soup = BeautifulSoup(page.content,'lxml')

        title = soup.find('h1',{'class':'prod-ProductTitle prod-productTitle-buyBox font-bold'}).get_text().strip()
    
        pricetmp = soup.find('span',{'class':'price-group'})
        dollars = pricetmp.find('span',{'class':'price-characteristic','itemprop':'price'}).get_text().strip()
        cents = pricetmp.find('span',{'class':'price-mantissa'}).get_text().strip()
        price = dollars + '.' + cents
        price = float(price)
        
        print(title)
        print(price)
    else:
        print("Page Not found")

def macysScraper(url):
    page = requests.get(url,headers = HEADERS)
    if page.status_code == 200:
        soup = BeautifulSoup(page.content,'lxml')

        title = soup.find('h1',{'class':'p-name h3','data-auto':'product-name'}).get_text().strip()

        pricetmp = soup.find('div',{'data-auto':'main-price'}).get_text().strip()
        pricetmp = pricetmp.split('$')
        price = float(pricetmp[1])
        
        try:
            saleprice = soup.find('span',{'class':'c-red medium-font bold on-sale','data-auto':'sale-price'}).get_text().strip()
            saleprice = saleprice.split(' ')
            saleprice = saleprice[1].split('$')
            saleprice = float(saleprice[1])
            print(saleprice)   
        except :
            print('No sale price')
        finally:
            print(title)
            print(price)
    else:
        print("Page Not found")


def saveData(websitename, url, price, date):
    pass

if __name__=='__main__':
    # amazonScraper('https://www.amazon.com/Sony-Noise-Cancelling-Headphones-WH1000XM3/dp/B07G4MNFS1/ref=sr_1_3?crid=NP0OOP8DWUN1&dchild=1&keywords=sony+wh-1000xm3&qid=1595736348&sprefix=sony%2Caps%2C257&sr=8-3')
    # amazonScraper('https://www.amazon.com/Razer-Kraken-Gaming-Headset-2019/dp/B07N86GL5T/ref=sr_1_2?crid=3HIY2AA2VTK2M&dchild=1&keywords=razer+kraken&qid=1595792235&sprefix=razer+kra%2Caps%2C150&sr=8-2')
    # bestBuyScraper('https://www.bestbuy.com/site/sony-wh-1000xm3-wireless-noise-cancelling-over-the-ear-headphones-with-google-assistant-black/6280544.p?skuId=6280544')
    # bestBuyScraper('https://www.bestbuy.com/site/lenovo-ideapad-1-14-laptop-amd-a6-series-4gb-memory-amd-radeon-r4-64gb-emmc-flash-memory-platinum-gray/6359222.p?skuId=6359222')
    # walmartScraper('https://www.walmart.com/ip/Sony-WH1000XM3-Wireless-Noise-Canceling-Over-the-Ear-Headphones-with-Google-Assistant-Black/931234733')
    macysScraper('https://www.macys.com/shop/product/dr.-scholls-womens-no-bad-vibes-sneakers?ID=7981139&CategoryID=13604&swatchColor=White')
