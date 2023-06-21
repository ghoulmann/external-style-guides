import requests
from bs4 import BeautifulSoup

def get_page_content(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')

def get_apple_terms(urls):
    terms = []
    for url in urls:
        soup = get_page_content(url)
        dts = soup.find_all('dt')
        for dt in dts:
            term = dt.text.strip()
            terms.append({"term": term, "url": url, "category": "Apple"})
    return terms

def get_google_terms(url):
    soup = get_page_content(url)
    terms = []
    dts = soup.find_all('dt')
    for dt in dts:
        term = dt.text.strip()
        anchor = dt.get('id')
        terms.append({"term": term, "url": url + '#' + anchor, "category": "Google"})
    return terms

def sort_terms(terms):
    return sorted(terms, key=lambda x: x['term'].lower())

def generate_markdown(terms):
    markdown = "# Word List\n\n"
    toc = "## Table of Contents\n\n"
    current_heading = None
    for term in terms:
        heading = term['term'][0].lower() if term['term'][0].isalpha() else 'Numbers and Symbols'
        if heading != current_heading:
            markdown += f"## {heading}\n\n"
            toc += f"- [{heading}](#{heading.lower()})\n"
            current_heading = heading
        if "pple" in term['category']:
            logo = "<img src='https://companieslogo.com/img/orig/AAPL-bf1a4314.png' height='12px'>" 
        else: 
            logo = "<img src='https://companieslogo.com/img/orig/GOOG-0ed88f7c.png' height='12px'>"
        markdown += f"**[{term['term']}]({term['url']})** &nbsp; {logo}\n\n"
    return toc + markdown

apple_urls = [
    "https://support.apple.com/guide/applestyleguide/numbers-apsgf82c6083/web",
    "https://support.apple.com/guide/applestyleguide/a-apsg3acde405/web",
    "https://support.apple.com/guide/applestyleguide/b-apsg1a3a0436/web",
    "https://support.apple.com/guide/applestyleguide/c-apsgb744e4a3/web",
    "https://support.apple.com/guide/applestyleguide/d-apsg7af4f5d0/web",
    "https://support.apple.com/guide/applestyleguide/e-apsg076a7313/web",
    "https://support.apple.com/guide/applestyleguide/f-apsg1d47a4df/web",
    "https://support.apple.com/guide/applestyleguide/g-apsg4104680a/web",
    "https://support.apple.com/guide/applestyleguide/h-apsg9dac5903/web",
    "https://support.apple.com/guide/applestyleguide/i-apsg346ef241/web",
    "https://support.apple.com/guide/applestyleguide/j-apsgf88bd162/web",
    "https://support.apple.com/guide/applestyleguide/k-apsgf9067ae8/web",
    "https://support.apple.com/guide/applestyleguide/l-apsg087a9dba/web",
    "https://support.apple.com/guide/applestyleguide/m-apsg72b28652/web",
    "https://support.apple.com/guide/applestyleguide/n-apsgb2f4a0d6/web",
    "https://support.apple.com/guide/applestyleguide/o-apsg9a401e4f/web",
    "https://support.apple.com/guide/applestyleguide/p-apsg4473eab0/web",
    "https://support.apple.com/guide/applestyleguide/q-apsg38496e66/web",
    "https://support.apple.com/guide/applestyleguide/r-apsgccfa0219/web",
    "https://support.apple.com/guide/applestyleguide/s-apsge70df12b/web",
    "https://support.apple.com/guide/applestyleguide/t-apsg841c3645/web",
    "https://support.apple.com/guide/applestyleguide/u-apsg45c3b57e/web",
    "https://support.apple.com/guide/applestyleguide/v-apsg51b3c806/web",
    "https://support.apple.com/guide/applestyleguide/w-apsg48ccd3b3/web",
    "https://support.apple.com/guide/applestyleguide/x-apsg3880fd94/web",
    "https://support.apple.com/guide/applestyleguide/y-apsg52ffc516/web",
    "https://support.apple.com/guide/applestyleguide/z-apsg5292fa92/web"
]


google_url = 'https://developers.google.com/style/word-list'

apple_terms = get_apple_terms(apple_urls)
google_terms = get_google_terms(google_url)

all_terms = sort_terms(apple_terms + google_terms)
markdown = generate_markdown(all_terms)

print(markdown)
