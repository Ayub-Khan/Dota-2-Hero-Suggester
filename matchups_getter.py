import scrapy
import os


class MatchupsGetter(scrapy.Spider):
    name = 'matchups_getter'

    def start_requests(self):
        with open('heros.txt', 'r') as f:
            for line in f:
                line = line.strip().lower().replace(" ", "-").replace("'", "")
                yield scrapy.Request(u'https://www.dotabuff.com/heroes/' + line + '/matchups?date=patch_7.06f',
                                     self.parse)

    def parse(self, response):
        title = response.css('title::text').extract()[0] + '.txt'
        machups = response.css('tr').css('td::attr(data-value)').extract()
        with open(title, 'wb') as f:
            for i in range(len(machups)/4):  # 4 is total number of columns
                f.write(machups[i*4] + "," + machups[i*4+1] + "," + machups[i*4+2] + "," + machups[i*4+3] + '\n')
