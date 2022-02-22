#import necessary modules
from flask import Flask, render_template
import json


# set up flask webserver
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


def load_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)


# define route(s)
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/scraping")
def scraping():
    data = load_json("data-to-scrape.json")
    return render_template("scraping.html", table=data)

@app.route("/results")
def results():
    return render_template("results.html")
    
# output to json
def write_json(data):
    with open("data.json", 'w') as f:
        json.dump(selector, f, indent=4)
     

# starts the webserver
if __name__ == "__main__":
    app.run()

# filter function
def my_filter(elem):
    return True

# creat the structure for the json file
selectors = []

# webscraping function
def my_scraper():
    def main():
    # get the URL in a useable form
    url = "http://localhost:5000/scraping"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # select your objects
    elements = [elem for elem in soup.select('.scrape-this')]

    print(f"Es wurden {len(elements)} Elemente gefunden.")

    data = []

    for i, elem in enumerate(elements):
        data.append({"id": i, "name": elem.text.strip()})


write_json(selectors)