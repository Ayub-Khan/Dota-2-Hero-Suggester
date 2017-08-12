import scrapy
import os

class MatchGetter(scrapy.Spider):
    name = 'match_getter'
    teams = {}

    def start_requests(self):
        for i in range(3228221453, 3216625224, -1):
            url = u'https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/?match_id=' \
                  + str(i) + '&key=2C892706E61FBB805E46E5A1E3F7CB26'
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        title = '/data/' + response.css('title::text').extract()[0] + '.txt'
        machups = response.css('tr').css('td::attr(data-value)').extract()
        with open(title, 'wb') as f:
            for i in range(len(machups)/4):  # 4 is total number of columns
                f.write(machups[i*4] + "," + machups[i*4+1] + "," + machups[i*4+2] + "," + machups[i*4+3] + '\n')
