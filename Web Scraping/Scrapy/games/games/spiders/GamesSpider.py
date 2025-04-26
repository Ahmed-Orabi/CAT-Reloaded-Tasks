import scrapy
from Games.items import GamesItem 

class GamesSpider(scrapy.Spider):
    name = "games"
    allowed_domains = ["sandbox.oxylabs.io"]
    start_urls = ["https://sandbox.oxylabs.io/products"]
    
    def parse(self, response):
        games = response.css("div.products-wrapper.css-phdzty.e1kord975")
        
        for game in games:
            item = GamesItem()
            item["title"] =       game.css("a h4::text").get() #
            item["category"] =    game.css("span.css-1pewyd6.eag3qlw8::text").get() #
            item["ratings"] =     len(game.css("div.rating.css-1lp4z4h.e15c0rei0").get())
            item["description"] = game.css("div p::text").get() #
            item["price"] =       game.css("div.price-wrapper.css-li4v8k.eag3qlw4::text").get() #
            item["stocks"] =      game.css("p.in-stock.css-1w904rj.eag3qlw1::text").get()
            
            yield {
                "title" :       game.css("a h4::text").get(), #
                "category" :    game.css("span.css-1pewyd6.eag3qlw8::text").get(), #
                "ratings" :     len(game.css("div.rating.css-1lp4z4h.e15c0rei0").get()),
                "description" : game.css("div p::text").get(), #
                "price" :       game.css("div.price-wrapper.css-li4v8k.eag3qlw4::text").get(), #
                "stocks" :      game.css("p.in-stock.css-1w904rj.eag3qlw1::text").get(),
            }
            
        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            next_page_url = "https://sandbox.oxylabs.io/products" + next_page
            yield response.follow(next_page_url, callback=self.parse)