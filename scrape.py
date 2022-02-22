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
    elements= [elem for elem in soup.select('.scrape-this')]
    print(f"Es wurden {len(elements)} Elemente gefunden.")
    soup.select=  bold 
    print(f"Es wurden {len(soup.select)} Elemente gefunden")

    Ich dachte, wenn ich schreibe zuerst schreibe, dass ich mit soup.select bold meine und
    bei print das gleiche schreibe wie beim vorherigen print und einfach elements mit soup. select tausche,
    würde das gehen.


    data = []

    for i, elemements in enumerate(elements):
        data.append({"id": i, "name": elem.text.strip()})
    

    with open("data.json", 'w') as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    main()
