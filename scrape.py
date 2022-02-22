# import necessary modules
from bs4 import BeautifulSoup
import requests
import json


def main():
    # get the URL in a useable form
    
    url = "http://localhost:5000/scraping"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    

    # select your objects - ich habe versucht, durch id(True) nur die Namen mit der Id true einzufügen

    elements = [elem for elem in soup.select('.scrape-this')]
    selectors = [True]

    print(f"Es wurden {len(elements)} Elemente gefunden.")

    data = []

    for i, elem in enumerate(elements):
        data.append({"id": i, "name": elem.text.strip()})


    

    with open("data.json", 'w') as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    main()
