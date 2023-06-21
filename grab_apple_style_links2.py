import requests
from bs4 import BeautifulSoup
from titlecase import titlecase

# Define your list of URLs with their respective categories

urls_with_categories = {
    "Writing inclusively": [
        "https://support.apple.com/guide/applestyleguide/intro-apdcb2a65d68/web",
        "https://support.apple.com/guide/applestyleguide/general-guidelines-apd91d6c2458/web",
        "https://support.apple.com/guide/applestyleguide/inclusive-representation-apd7a037f274/web",
        "https://support.apple.com/guide/applestyleguide/gender-identity-apd2a7af8d36/web",
        "https://support.apple.com/guide/applestyleguide/writing-about-disability-apd49cbb2b06/web"
    ],
    "Units of measure": [
        "https://support.apple.com/guide/applestyleguide/intro-apsg6ae856d6/web",
        "https://support.apple.com/guide/applestyleguide/prefixes-for-units-of-measure-apsg1fb1fd8b/web",
        "https://support.apple.com/guide/applestyleguide/names-and-unit-symbols-for-units-of-measure-apsg1fb1fcb1/web"
    ],
    "Technical notation": [
        "https://support.apple.com/guide/applestyleguide/intro-apsgf72184e0/web",
        "https://support.apple.com/guide/applestyleguide/code-apsg1fde748e/web",
        "https://support.apple.com/guide/applestyleguide/syntax-descriptions-apsg1fde7568/web",
        "https://support.apple.com/guide/applestyleguide/code-font-in-text-apsg1fde73a3/web",
        "https://support.apple.com/guide/applestyleguide/placeholder-names-in-text-apsg1fde72a8/web"
    ],
    "International style": [
        "https://support.apple.com/guide/applestyleguide/intro-apsg1ff68ab5/web",
        "https://support.apple.com/guide/applestyleguide/countries-apd48c19cb1f/web",
        "https://support.apple.com/guide/applestyleguide/currency-apsg1ff68c48/web",
        "https://support.apple.com/guide/applestyleguide/dates-and-times-apsg1ff687a0/web",
        "https://support.apple.com/guide/applestyleguide/decimals-apsg1ff68b7e/web",
        "https://support.apple.com/guide/applestyleguide/languages-apsg1ff6873c/web",
        "https://support.apple.com/guide/applestyleguide/telephone-numbers-apsg1ff68be3/web",
        "https://support.apple.com/guide/applestyleguide/units-of-measure-apsg1ff689db/web"
    ]
}


# Initialize the output dictionary
output_dict = {}

for category, urls in urls_with_categories.items():
    output_dict[category] = {}
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the h1 text
        h1_text = f"[{titlecase(soup.find('h1').text.strip())}]({url})"
        
        # Extract h2 tags and generate a list of their texts along with the respective URLs
        h2_elements =  soup.find_all("h2", {"class": "Name"})

        h2_links = []

        for h2 in h2_elements:
            h2_text = h2.text.strip().replace(".", "")
            # Check if h2 tag has an id for anchor link
            
            h2_link = f"[{h2_text}]({url})"
            if h2_link:
                h2_links.append(h2_link)
            
        output_dict[category][h1_text] = h2_links


# Print the output dictionary
for category, data in output_dict.items():
    print(f"## {category}\n")
    for h1_text, h2_links in data.items():
        if h2_links:
            print(f"**{h1_text}**: {', '.join(h2_links)}\n")
        else:
            print(f"**{h1_text}**\n")
