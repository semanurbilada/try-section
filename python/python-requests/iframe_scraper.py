import requests
from bs4 import BeautifulSoup
# Import urljoin function to construct absolute URLs
from urllib.parse import urljoin  

# PURPOSE: Find div tag's content from website structured by iframe

url = "actual website url"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the iframe element
    iframe = soup.find('iframe')

    if iframe:
        # Extract the src attribute from the iframe
        iframe_src = iframe.get('src')

        if iframe_src:
            # Construct the absolute URL
            absolute_url = urljoin(url, iframe_src)

            # Make a new request to the absolute URL
            iframe_response = requests.get(absolute_url)

            if iframe_response.status_code == 200:
                iframe_soup = BeautifulSoup(iframe_response.text, 'html.parser')

                # Find the div inside the iframe
                word_section_div = iframe_soup.find('div', {'class': 'actual className for specific div'})

                if word_section_div:
                    # Extract the text content
                    text_content = word_section_div.get_text()
                    print(text_content)
                else:
                    print("Div not found inside the iframe.")
            else:
                print(f"Failed to get content from iframe. Status code: {iframe_response.status_code}")
        else:
            print("src attribute not found in the iframe.")
    else:
        print("Iframe not found on the main page.")
else:
    print(f"Failed to get main page. Status code: {response.status_code}")