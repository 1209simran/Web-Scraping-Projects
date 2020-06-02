import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

title = soup.title
# print(type(title.string))

paras = soup.find_all('p')
# print(paras)

# print(soup.find('p')['class'])
# print(soup.find_all('p', class_="lead"))
# print(soup.find('p').get_text())

anchors = soup.find_all('a')
all_links = set()

for link in anchors:
    if(link.get('href') != '#'):
        linktext = "https://codewithharry.com"+link.get('href')
        all_links.add(linktext)
        # print(linktext)

# print(all_links)

markup = "<p><!--comment --></p>"
soup2 = BeautifulSoup(markup)
# print(type(soup2.string))

navbarSupportContent = soup.find(id="navbarSupportedContent")

# for elem in navbarSupportContent.contents:
#     print(elem)


# for elem in navbarSupportContent.stripped_strings:
#     print(elem)

# print(navbarSupportContent.parent)


# for elem in navbarSupportContent.parents:
#     print(elem.name)

# print(navbarSupportContent.previous_sibling.previous_sibling)

elem = soup.select('.modal-footer')
print(elem)
