import requests
from bs4 import BeautifulSoup

URL = "https://cars.kg/offers?direction=sale&vendor=57fa24ee2860c45a2a2c08ac&model=&generation=&serie=&modification=&price_from=&price_to=&year_from=&year_to=2022&running_length_from=&running_length_to=&kuzov=&capacity_from=&capacity_to=&color=&city="
HEADERS = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "accept": "*/*"
}
# Returns an html text of cars of cars.kg


def get_cars_list_html(some_url, some_headers):
    response = requests.get(url=some_url, headers=some_headers)
    return response

# Creates list of info from html about cars


def get_content_from_html(html_converted_to_text):
    soup = BeautifulSoup(html_converted_to_text, "html.parser")
    cars_html_objects_from_html = soup.find_all("a", class_="catalog-list-item")
    cars_objects_list = []
    cars_kg_endpoint = "https://cars.kg"

    for each_car_object in cars_html_objects_from_html:
        if each_car_object.find("span", class_="catalog-item-mileage") == "":
            cars_objects_list.append(
                {
                    "car_model": each_car_object.find("span", class_="catalog-item-caption").get_text().replace("\n", "").strip(),
                    "car_description": each_car_object.find("span", class_="catalog-item-descr").get_text().replace("\n", "").strip(),
                    "car_year": each_car_object.find("span", class_="caption-year").get_text().replace("\n", "").strip(),
                    "car_price": each_car_object.find("span", class_="catalog-item-price").get_text().replace("\n", "").strip(),
                    "car_date_and_address": each_car_object.find("span", class_="catalog-item-info").get_text().replace("\n", "").strip(),
                    "car_mileage": "Not specified"
                }
            )
        else:
            cars_objects_list.append(
                {
                    "car_model": each_car_object.find("span", class_="catalog-item-caption").get_text().replace("\n", "").strip(),
                    "car_description": each_car_object.find("span", class_="catalog-item-descr").get_text().replace("\n", "").strip(),
                    "car_year": each_car_object.find("span", class_="caption-year").get_text().replace("\n", "").strip(),
                    "car_price": each_car_object.find("span", class_="catalog-item-price").get_text().replace("\n", "").strip(),
                    "car_date_and_address": each_car_object.find("span", class_="catalog-item-info").get_text().replace("\n", "").strip(),
                    "car_mileage": each_car_object.find("span", class_="catalog-item-mileage").get_text().replace("\n", "").strip()
                }
            )

    print(cars_objects_list)


def parse_cars_kg():
    html = get_cars_list_html(some_url=URL, some_headers=HEADERS)
    if html.status_code == 200:
        get_content_from_html(html.text)


parse_cars_kg()


