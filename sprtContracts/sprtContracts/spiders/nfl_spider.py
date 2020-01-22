import scrapy
from sprtContracts.items import SprtcontractsItem


class NFLSpider(scrapy.Spider):
    name = "nfl_spider"
    allowed_urls = ['www.spotrac.com']
    start_urls = ['https://www.spotrac.com/nfl/contracts/#']

    def parse(self, response):
        """

        :param response: response object from visiting the NFL 2020 contracts page from spottrac
        :return: a dictionary-like object representing a player's contractual information
        """
        players = response.xpath('//tr')

        # first table row is the table header
        for player in players[1:]:
            name = player.xpath('.//a/text()').extract_first()
            position = player.xpath('./td[2]/text()').extract_first()
            team = player.xpath('./td[3]/text()').extract_first()
            currentAge = player.xpath('./td[4]/text()').extract_first()
            totalYears = player.xpath('./td[5]/text()').extract_first()
            totalAmount = player.xpath('./td[6]/span/text()').extract_first()
            avgAmount = player.xpath('./td[7]/text()').extract_first()
            grtAmount = player.xpath('./td[8]/text()').extract_first()
            practicalGrt = player.xpath('./td[9]/text()').extract_first()
            grtSigning = player.xpath('./td[10]/text()').extract_first()
            faYear = player.xpath('./td[11]/text()').extract_first()
            yrRange = player.xpath('./td[1]/span[2]/text()').extract_first()
            ageAtBeg = player.xpath('./@data-age-signed').extract_first()

            item = SprtcontractsItem()
            item['name'] = name
            item['position'] = position
            item['team'] = team
            item['currentAge'] = currentAge
            item['totalYears'] = totalYears
            item['totalAmount'] = totalAmount
            item['avgAmount'] = avgAmount
            item['grtAmount'] = grtAmount
            item['practicalGrt'] = practicalGrt
            item['grtSigning'] = grtSigning
            item['faYear'] = faYear
            item['yrRange'] = yrRange
            item['ageAtBeg'] = ageAtBeg
            yield item
