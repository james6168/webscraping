import requests
from bs4 import BeautifulSoup

URL = "https://cars.kg/offers"
HEADERS = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "accept": "*/*"
}
# Returns an html text of cars of cars.kg

def get_cars_list_hmtl(some_url, some_headers):
    response = requests.get(url=some_url, headers=some_headers)
    return response

# Creates list of info from html about cars

def get_content_from_html(html_converted_to_text):
    soup = BeautifulSoup(html_converted_to_text, "html.parser")
    cars_html_objects_from_html = soup.find_all("a", class_="catalog-list-item")
    cars_objects_list = []
    cars_kg_endpoint = "https://cars.kg"

    for each_car_object in cars_html_objects_from_html:
        cars_objects_list.append(
            {
                "car_model": each_car_object.find("span", class_="catalog-item-caption"),
                "car_description": each_car_object.find("span", class_="catalog-item-descr"),

            }
        )


