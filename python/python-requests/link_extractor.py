import requests
from bs4 import BeautifulSoup

# PURPOSE: Find all the a tag content from web page

url = "https://github.com/semanurbilada"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all("a")

    for link in links:
        print(link.get("href"))
else:
    print(f"Failed to fetch content. Status code: {response.status_code}")