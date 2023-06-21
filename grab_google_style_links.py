import requests
from bs4 import BeautifulSoup
#import nltk
#from nltk.tokenize import sent_tokenize
#nltk.download('punkt')
#from summa.summarizer import summarize
import re
import titlecase
import json
from pprint import pprint


def create_bib_entry(url, title):
    return f'**[{titlecase.titlecase(title)}]({url})**'

# Scrape the main page for links
main_page_url = 'https://developers.google.com/style'
response = requests.get(main_page_url)
soup = BeautifulSoup(response.text, 'html.parser')
print(f"## {titlecase.titlecase('Google developer documentation style guide')}\n")
# Assume that the links are within <a> tags
links = soup.find_all('a')
entries = {}
items = []
for link in links:
    url = link.get('href')
    # Check if the link is to a page within the style guide
    
    if url.startswith('/style/'):
        #url = main_page_url + url
        title = link.get_text()
        
        
        output = create_bib_entry("https://developers.google.com" + url, title)
        section = create_bib_entry("https://developers.google.com" + url, title)
        response = requests.get("https://developers.google.com" + url)
        page = BeautifulSoup(response.text, 'html.parser')
        #print(summarize(page.get_text(), words=50))
        headings = []
        for h in page.find_all(re.compile("h2")):
            headings.append(f"[{h.text.strip()}](https://developers.google.com{url}#{h.get('id')})")
        if headings:
            output += (f': {"; ".join(headings)}\n')
            entries[section] = headings
        else:
            output += "\n"
            entries[section] = ""
        items.append(output)
items = set(items)

items = sorted(items)

def print_from_list(items):
    for item in items:
        print(item)
#print(len(entries.keys()), len(entries.values()))
#json_object = json.dumps(entries, indent=4)

def print_dict(entries):
    for entry in sorted(entries.items()):
        if type(entry[1]) == list:
            print(entry[0], "; ".join(entry[1]) + "\n", sep=": ")
        else:
            print(entry[0], "\n")

print_dict(entries)