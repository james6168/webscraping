import requests
from bs4 import BeautifulSoup

URL = "https://www.kivano.kg/noutbuki?brands=acer-apple"
HEADERS = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "accept": "*/*"
}

def get_html(url, header):
    response = requests.get(url=url, headers=header)
    return response

def get_content_from_html(html_text):
    soup = BeautifulSoup(html_text, "html.parser")
    items = soup.find_all("div", class_="item product_listbox oh")
    laptops = []
    LINK = "https://www.kivano.kg"

    for item in items:
        laptops.append(
            {
                "title": item.find("div", class_="listbox_title oh").get_text().replace("\n", ""),
                "description": item.find("div", class_="product_text pull-left").get_text().replace("\n", ""),
                "price": item.find("div", class_="listbox_price text-center").get_text().replace("\n", ""),
                "image": LINK + item.find("img").get("src")
            }
        )
    print(laptops)

def get_result_parse():
    html = get_html(url=URL, header=HEADERS)
    if html.status_code == 200:
        get_content_from_html(html.text)

get_result_parse()
