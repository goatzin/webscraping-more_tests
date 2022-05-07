# Hello O_o
from bs4 import BeautifulSoup
import requests

# Amazon website
response = requests.get("https://www.amazon.com.br/gp/bestsellers/books/?ie=UTF8&ref_=sv_b_2") # bestselling books page
print("choose rating 0 to 5:") # This will filter only the numbers above the chosen one
rating = float(input(">"))
print(f"Filtering out {rating}")

html_doc = response.content
soup = BeautifulSoup(html_doc, "lxml")
books = soup.find_all("div", "zg-grid-general-faceout")

for book in books: 
    title = book.find("div", "_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y").text
    author = book.find("div", "a-row a-size-small").findChild("div", "_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y").text
    stars = float(book.find("span", "a-icon-alt").string.split(' ')[0].replace(',', '.'))
    if stars >= rating:
        print(f"title: {title}")
        print(f"author: {author}")
        print(f"rating: {stars}")
        print("")

