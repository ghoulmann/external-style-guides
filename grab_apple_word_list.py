import requests
from bs4 import BeautifulSoup

urls = [
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


data = {}

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the H1 text
    h1_text = soup.find('h1').text

    # Extract all dt elements
    dt_elements = [f"[{dt.text}]({url})" for dt in soup.find_all('dt')]

    # Add to the dictionary
    data[f"[{h1_text}]({url})"] = dt_elements

def print_dict(data):
    for entry in sorted(data.items()):
        if type(entry[1]) == list:
            print(f'### {entry[0]}',"; ".join(entry[1]), sep="\n\n")
        else:
            print(entry[0], "\n")
print("## Style and Usage A-Z (Apple Style Guide)\n")
print_dict(data)