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
main_page_url = 'https://support.apple.com/guide/applestyleguide/welcome/web'
response = requests.get(main_page_url)
soup = BeautifulSoup(response.text, 'html.parser')
print(f"## {titlecase.titlecase('Apple style guide')}\n")
# Assume that the links are within <a> tags
links = soup.find_all('a')
entries = {}
items = []
for link in links:
    url = link.get('href')
    # Check if the link is to a page within the style guide


    try:
        if "applestyleguide" in url:
            
            
            title = link.get_text()


            output = create_bib_entry(url, title)
            section = create_bib_entry(url, title)
            response = requests.get(url)
            page = BeautifulSoup(response.text, 'html.parser')
            #print(summarize(page.get_text(), words=50))
            headings = []
            for h in page.find_all(re.compile("h2")):
                headings.append(f"[{h.text.strip()}]({url}#{h.get('id')})")
            if headings:
                output += (f': {"; ".join(headings)}\n')
                entries[section] = headings
            else:
                output += "\n"
                entries[section] = ""
            items.append(output)
    except TypeError as e:
        pass    
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
print_from_list(items)
