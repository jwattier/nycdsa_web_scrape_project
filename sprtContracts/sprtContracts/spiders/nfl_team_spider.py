import scrapy
from sprtContracts.items import NflteamItem

class NFLSpider(scrapy.Spider):
    name = "nfl_team_spider"
    allowed_urls = ['www.spotrac.com']
    start_urls = ['https://www.spotrac.com/nfl/arizona-cardinals/cap/2019/']

    def parse(self, response):
        # TODO: condense code to loop through a dictionary of lists
        # TODO: add url loop with years 2007 to 2021 and with all teams
        # base_url = 'https://www.spotrac.com/nfl/'
        # year_range = list(range(2007, 2021))
        # team_list
        #
        team = 'Arizona Cardinals'
        year = '2019'

        active_players = response.xpath('//table[1]/tbody/tr')
        for player in active_players:
            roster_status = 'active'
            name = player.xpath('./td[1]/a/text()').extract_first()
            position = player.xpath('./td[2]/span/text()').extract_first()
            base_salary = player.xpath('./td[3]/span/text()').extract_first()
            signing_bonus = player.xpath('./td[4]/span/text()').extract_first()
            roster_bonus = player.xpath('./td[5]/span/text()').extract_first()
            option_bonus = player.xpath('./td[6]/span/text()').extract_first()
            workout_bonus = player.xpath('./td[7]/span/text()').extract_first()
            restruct_bonus = player.xpath('./td[8]/span/text()').extract_first()
            other_bonus = player.xpath('./td[9]/span/text()').extract_first()
            dead_cap_amt = player.xpath('./td[5]/span/text()').extract_first()
            cap_hit = player.xpath('./td[11]/span/text()').extract_first()
            cap_perc = player.xpath('./td[12]/text()').extract_first()

            item = NflteamItem()
            item['team'] = team
            item['year'] = year
            item['roster_status'] = roster_status
            item['name'] = name
            item['position'] = position
            item['base_salary'] = base_salary
            item['signing_bonus'] = signing_bonus
            item['roster_bonus'] = roster_bonus
            item['option_bonus'] = option_bonus
            item['workout_bonus'] = workout_bonus
            item['restruct_bonus'] = restruct_bonus
            item['other_bonus'] = other_bonus
            item['dead_cap_amt'] = dead_cap_amt
            item['cap_hit'] = cap_hit
            item['cap_perc'] = cap_perc
            yield item

        dead_cap_players = response.xpath("//h2[contains(text(), 'Dead Cap')]/following::table[1]/tbody/tr")
        if dead_cap_players:
            for player in dead_cap_players:
                roster_status = 'dead_cap'
                name = player.xpath('./td[1]/a/text()').extract_first()
                position = player.xpath('./td[2]/span/text()').extract_first()
                base_salary = player.xpath('./td[3]/span/text()').extract_first()
                signing_bonus = player.xpath('./td[4]/span/text()').extract_first()
                roster_bonus = player.xpath('./td[5]/span/text()').extract_first()
                option_bonus = player.xpath('./td[6]/span/text()').extract_first()
                workout_bonus = player.xpath('./td[7]/span/text()').extract_first()
                restruct_bonus = player.xpath('./td[8]/span/text()').extract_first()
                other_bonus = player.xpath('./td[9]/span/text()').extract_first()
                dead_cap_amt = player.xpath('./td[5]/span/text()').extract_first()
                cap_hit = player.xpath('./td[11]/span/text()').extract_first()
                cap_perc = player.xpath('./td[12]/text()').extract_first()

                item = NflteamItem()
                item['team'] = team
                item['year'] = year
                item['roster_status'] = roster_status
                item['name'] = name
                item['position'] = position
                item['base_salary'] = base_salary
                item['signing_bonus'] = signing_bonus
                item['roster_bonus'] = roster_bonus
                item['option_bonus'] = option_bonus
                item['workout_bonus'] = workout_bonus
                item['restruct_bonus'] = restruct_bonus
                item['other_bonus'] = other_bonus
                item['dead_cap_amt'] = dead_cap_amt
                item['cap_hit'] = cap_hit
                item['cap_perc'] = cap_perc
                yield item

        injured_players = response.xpath("//h2[contains(text(), 'Injured Reserve Cap')]/following::table[1]/tbody/tr")
        if injured_players:
            for player in injured_players:
                roster_status = 'injured'
                name = player.xpath('./td[1]/a/text()').extract_first()
                position = player.xpath('./td[2]/span/text()').extract_first()
                base_salary = player.xpath('./td[3]/span/text()').extract_first()
                signing_bonus = player.xpath('./td[4]/span/text()').extract_first()
                roster_bonus = player.xpath('./td[5]/span/text()').extract_first()
                option_bonus = player.xpath('./td[6]/span/text()').extract_first()
                workout_bonus = player.xpath('./td[7]/span/text()').extract_first()
                restruct_bonus = player.xpath('./td[8]/span/text()').extract_first()
                other_bonus = player.xpath('./td[9]/span/text()').extract_first()
                dead_cap_amt = player.xpath('./td[5]/span/text()').extract_first()
                cap_hit = player.xpath('./td[11]/span/text()').extract_first()
                cap_perc = player.xpath('./td[12]/text()').extract_first()

                item = NflteamItem()
                item['team'] = team
                item['year'] = year
                item['roster_status'] = roster_status
                item['name'] = name
                item['position'] = position
                item['base_salary'] = base_salary
                item['signing_bonus'] = signing_bonus
                item['roster_bonus'] = roster_bonus
                item['option_bonus'] = option_bonus
                item['workout_bonus'] = workout_bonus
                item['restruct_bonus'] = restruct_bonus
                item['other_bonus'] = other_bonus
                item['dead_cap_amt'] = dead_cap_amt
                item['cap_hit'] = cap_hit
                item['cap_perc'] = cap_perc
                yield item

