from bs4 import BeautifulSoup
import requests

def create_dict_from_webpage(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data_dict = {}
    current_h3 = ""

    for tag in soup.find_all(['h3', 'dt']):
        if tag.name == 'h3':
            current_h3 = tag.get_text()
            data_dict[current_h3] = []
        elif tag.name == 'dt':
            term = tag.get_text().strip()
            anchor = tag.get('id')
            data_dict[current_h3].append(f"[{term}](https://developers.google.com/style/word-list#{anchor})")

    return data_dict

url = "https://developers.google.com/style/word-list"
data = create_dict_from_webpage(url)

print("## Word List (Google Developer Documentation Style Guide)")
def print_dict(data):
    for entry in sorted(data.items()):
        if type(entry[1]) == list:
            print(f'\n### {entry[0]}',"; ".join(entry[1]), sep="\n\n")
        else:
            print(entry[0], "\n")
print("## Style and Usage A-Z (Apple Style Guide)\n")
print_dict(data)

