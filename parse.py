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

# Function get_nbkr_usd_to_kgs_rate() returns a float of USD currency rate to KGS


def get_nbkr_usd_to_kgs_rate():
    import xml.etree.ElementTree as ET
    response_string = requests.get("https://www.nbkr.kg/XML/daily.xml").text.replace("\n", "")
    response_xml = ET.fromstring(response_string.encode("windows-1251"))
    usd_to_kgs_rate = float(response_xml.findtext(".//Currency[@ISOCode='USD']//Value").replace(",", "."))
    return usd_to_kgs_rate


def get_content_from_html(html_text):
    soup = BeautifulSoup(html_text, "html.parser")
    items = soup.find_all("div", class_="item product_listbox oh")
    laptops = []
    LINK = "https://www.kivano.kg"
    nbkr_usd_float = get_nbkr_usd_to_kgs_rate()

    for item in items:
        laptops.append(
            {
                "title": item.find("div", class_="listbox_title oh").get_text().replace("\n", ""),
                "description": item.find("div", class_="product_text pull-left").get_text().replace("\n", ""),
                "price": item.find("div", class_="listbox_price text-center").get_text().replace("\n", ""),
                "price_usd": str(float(item.find("div", class_="listbox_price text-center").get_text().replace("\n", "").replace(" сом", "")) / nbkr_usd_float) + " USD",
                "image": LINK + item.find("img").get("src")
            }
        )
    print(laptops)


def get_result_parse():
    html = get_html(url=URL, header=HEADERS)
    if html.status_code == 200:
        get_content_from_html(html.text)


get_result_parse()


# print(get_nbkr_usd_to_kgs_rate())
