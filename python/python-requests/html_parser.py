import requests
#beautifulsoup, bs4, lxml and html5lib installed by pip3;
from bs4 import BeautifulSoup 

# PURPOSE: HTML parser

session = requests.Session()

pageUrl = "https://github.com/semanurbilada"

page = session.get(pageUrl)

page_content = page.content

# BeautifulSoup(page_content, "html-parser") changed to lxml because of an ERROR;
soup = BeautifulSoup(page_content, "lxml")

print(page.status_code)

file = open("parsed.html", "w", encoding="utf-8")
file.write(str(soup))
file.close()