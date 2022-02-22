# import necessary modules
from bs4 import BeautifulSoup
import requests
import json


def main():
    # get the URL in a useable form
    url = "http://localhost:5000/scraping"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # select your objects
    def f_func(item):
        if strong(item) == True:
            return True
        return False

    
    elements = [elem for elem in soup.select('.scrape-this')]


    print(f"Es wurden {len(list(filter(f_func, elements)))} Elemente gefunden.")

    data = []

    for i, elem in enumerate(elements):
        data.append({"id": i, "name": elem.text.strip()})

    with open("data.json", 'w') as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    main()
