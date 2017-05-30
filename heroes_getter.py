import scrapy


# class QuotesSpider(scrapy.Spider):
#     name = "quotes"
#     start_urls = [
#         'http://quotes.toscrape.com/tag/humor/',
#     ]
#
#     def parse(self, response):
#         for quote in response.css('div.quote'):
#             yield {
#                 'text': quote.css('span.text::text').extract_first(),
#                 'author': quote.xpath('span/small/text()').extract_first(),
#             }
#
#         next_page = response.css('li.next a::attr("href")').extract_first()
#         if next_page is not None:
#             next_page = response.urljoin(next_page)
#             yield scrapy.Request(next_page, callback=self.parse)

class HeroGetter(scrapy.Spider):
    name = "heroes_getter"
    start_urls = [
        'https://www.dotabuff.com/heroes',
    ]

    def parse(self, response):
        heroes = response.css('div.hero-grid').css('div.name::text').extract()
        with open('heroes.txt', 'wb') as f:
            for hero in heroes:
                f.write(hero+'\n')
        # for name in (response.css('div.hero-grid')).css('div.name'):
        #     self.heroes.append(name.xpath('text()').extract_first())
        #     # yield {
        #     #     'name': name.xpath('text()').extract_first(),
        #     # }



