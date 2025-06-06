# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class GamesItem(scrapy.Item):
    title = Field() 
    category = Field() 
    ratings = Field()
    description = Field()
    price = Field()
    stocks = Field()
