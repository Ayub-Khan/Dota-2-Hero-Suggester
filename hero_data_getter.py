import scrapy
import os


class HeroDataGetterOne(scrapy.Spider):
    name = 'matchups_getter'

    def start_requests(self):
        with open('heros.txt', 'r') as f:
            for line in f:
                line = line.strip().lower().replace(" ", "-").replace("'", "")
                yield scrapy.Request(u'https://www.dotabuff.com/heroes/' + line,
                                     self.parse)

    def parse(self, response):
        file = open("hero_data.txt", "a+")
        name = (response.css('title::text').extract()[0]).split('-')[0].strip()
        data = response.css("div.header-content-title").css("small::text").extract()[0].split(',')
        hero_type = ""
        if response.css("tbody.primary-agility").extract() != []:
            hero_type = "Agility"
        elif response.css("tbody.primary-intelligence").extract() != []:
            hero_type = "Intelligence"
        else:
            hero_type = "Strength"
        lane_details = str(response.css('tbody')[1].css('tr').css('td::text').extract())
        attack_type = data[0]
        roles = ""
        for item in data[1:]:
            roles += '|' + item.strip()
        file.write(name + '|' + hero_type + '|' + attack_type + roles + '|' + lane_details + '\n')
        file.close()
