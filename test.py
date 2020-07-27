import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/Auriculares-inal%C3%A1mbricos-WH1000XM3-cancelaci%C3%B3n-auriculares/dp/B07G4MNFS1/ref=sr_1_1_sspa?crid=1CPOOW3I0CBDS&dchild=1&keywords=sony+wh-1000xm3&qid=1595788032&sprefix=sony%2Caps%2C147&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFaRTdGMlZMUDFIUkkmZW5jcnlwdGVkSWQ9QTAzOTI2NTdUTUw4UkM3TU9XWDEmZW5jcnlwdGVkQWRJZD1BMDQ1NTM2NzJVQlRYQUlTTUU0WEEmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl"
HEADERS = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}

def getTitle():
    page = requests.get(URL,headers=HEADERS)
    print(page.status_code)
    soup = BeautifulSoup(page.content, 'lxml')

    title = soup.find(id = "productTitle").get_text().strip()
    price = soup.find(id = "priceblock_ourprice").get_text().strip()
    print(title)
    print(price)


if __name__ == "__main__":
    getTitle()