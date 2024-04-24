from bs4 import BeautifulSoup
import requests
import json


def load_json_data(URL):
    r = requests.get(URL)

    soup_without = BeautifulSoup(r.content, "html.parser")

    json_data = json.loads(str(soup_without))

    created_file = "flights_information.json"

    with open(created_file, "w") as file:
        json.dump(json_data, file)
        print(f"JSON data saved in a {created_file}")

    with open(created_file, "r") as file:
        data = json.load(file)
        print(f"JSON data for the provided URL :\n {data}")


step_1 = "http://homeworktask.infare.lt/search.php?from=MAD&to=AUH&depart=2024-05-02&return=2024-05-10"

URL = step_1

load_json_data(URL)
