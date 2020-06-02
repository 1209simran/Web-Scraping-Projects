import requests
from bs4 import BeautifulSoup
url = "https://www.flipkart.com/search?p%5B%5D=facets.brand%255B%255D%3DSamsung&sid=tyy%2F4io&sort=recency_desc&wid=1.productCard.PMU_V2_1"

r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup)

containers = soup.find_all("div", class_="_1UoZlX")
# print(BeautifulSoup.prettify(containers[0]))
# print(containers[0])

# for elem in containers:
#     print(elem.img["alt"])
price_container = soup.find_all("div", class_="_1vC4OE _2rQ-NK")
# print(price_container[0].text)

rating_container = soup.find_all("div", class_="hGSR34")
# print(rating_container[0].text)

filename = "products.csv"
f = open(filename, "w")

headers = "Product_Name, Price, Rating \n"
f.write(headers)

for elem in containers:
    Product_Name = elem.img["alt"]
    Price = elem.find_all("div", class_="_1vC4OE _2rQ-NK")
    Rating = elem.find_all("div", class_="hGSR34")
    # print(Product_Name)
    # print(Price[0].text)
    finalRating = "NULL"
    if(Rating):
        finalRating = Rating[0].text
    # print(finalRating)
    f.write(Product_Name.replace(",", " |")+"," +
            Price[0].text.replace(",", "")+","+finalRating+"\n")

f.close()
