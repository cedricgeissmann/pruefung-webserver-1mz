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
    elements = [elem for elem in soup.select('.scrape-this, strong=true')]

    print(f"Es wurden {len(elements)} Elemente gefunden.")

    data = []

    for i, elem in enumerate(elements):
        data.append({"id": i, "name": elem.text.strip()})

    with open("data.json", 'w') as f:
        json.dump(data, f, indent=4)

for row in table_rows:
    cells = list(row.select('td'))
    if cells:
        entry = {
            'selector': "placeholder text, which will be overwritten below",
            'example': cells[1].text,
            'description': cells[2].text,
            
        }
        # we need the following code beacause not all entries in the first column are text - some are links (a-tag)
        if cells[0].strong:
            entry['selector'] = cells[0].strong.text
        else:
            entry['selector'] = cells[0].text

# define filter function
def filter_func(elem):
    return True

# apply filter function
table_rows = list(filter(filter_func, table_rows))

selectors = []



if __name__ == "__main__":
    main()
