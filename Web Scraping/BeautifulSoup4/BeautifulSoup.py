import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

titles = []
developers = []
platforms = []
types = []
prices = []
ratings = []
stocks = []
des = []

limit = 3000
i = 1
while i <= limit:
    url = f"https://sandbox.oxylabs.io/products/{i}"
    result = requests.get(url) # Fetch URL
    source = result.text
    soup = BeautifulSoup(source, "html.parser") # Parse content from source
    # print(soup.prettify())

    try:
        game_title = soup.find_all("h2", {"class" : "title css-1k75zwy e1pl6npa11"})
        titles.append(game_title[0].text)

        developer_brand = soup.find('span', class_='brand developer').get_text(strip=True).replace("Developer:", "").strip("'").strip()
        developers.append(developer_brand)

        # game_platform = soup.find_all("span", {"class" : "game-platforms-wrapper"})
        # print(game_platform)

        game_type = soup.find("div", {"class" : "brand-wrapper css-1f150rr e15c0rei0"})
        typeExtracted = game_type.get_text().split(":")
        types.append(typeExtracted[-1])

        game_price = soup.find_all("div", {"class" : "price css-o7uf8d e1pl6npa6"})
        prices.append(game_price[0].text)

        availability = soup.find_all("p", {"class" : "availability css-qequvl e1pl6npa1"})
        stocks.append(availability[0].text)

        #game_ratings = soup.find_all('div', class_="product-info-wrapper css-m2w3q2 emlf3670")
        #print(game_ratings)

        description = soup.find_all("p", {"class" : "description css-mkw8pm e1pl6npa0"})
        des.append(description[0].text)

        # game_genre = soup.find_all("div", {"class" : "genre css-w9wtzg e1pl6npa9"})
        # print(game_genre)
    except:
        print(f"Error in product {i}")
    i += 1
    

with open('games.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Game Title", "Developer", "Type", "Price"])
    for i in range(len(titles)):
        writer.writerow([titles[i], developers[i],types[i],prices[i]])  