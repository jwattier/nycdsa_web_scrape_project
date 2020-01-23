from scrapy import Spider
from sprtContracts.items import NflteamItem
from collections import defaultdict
import pandas as pd


class NFLSpider(Spider):
    name = "nfl_team_spider"
    allowed_urls = ['www.spotrac.com']
    list_of_teams = pd.read_csv('nfl_teams_url_format.csv', header=None, names=['team_name'])['team_name'].to_list()
    # base_url = "https://www.spotrac.com/nfl/"
    start_urls = [
        "https://www.spotrac.com/nfl/" + team + '/cap/' + str(year) + '/'
        for team in list_of_teams
        for year in list(range(2007, 2021))
    ]
    #  start_urls = ['https://www.spotrac.com/nfl/arizona-cardinals/cap/2019/',
    #              "https://www.spotrac.com/nfl/arizona-cardinals/cap/2020/",]

    def parse(self, response):
        players_on_page = defaultdict(list)
        active_players = response.xpath('//table[1]/tbody/tr')
        injured_players = response.xpath("//h2[contains(text(), 'Injured Reserve Cap')]/following::table[1]/tbody/tr")
        nfinj_players = response.xpath("//h2[contains(text(), 'Non-Football Injury Cap')]/following::table[1]/tbody/tr")
        ps_players = response.xpath("//h2[contains(text(), 'Practice Squad')]/following::table[1]/tbody/tr")
        dead_cap_players = response.xpath("//h2[contains(text(), 'Dead Cap')]/following::table[1]/tbody/tr")

        if active_players:
            players_on_page['active'] = active_players
        if injured_players:
            players_on_page['injured_reserve'] = injured_players
        if nfinj_players:
            players_on_page['non_fb_injury'] = nfinj_players
        if ps_players:
            players_on_page['practice_squad'] = ps_players
        if dead_cap_players:
            players_on_page['dead_cap'] = dead_cap_players

        for player_type in players_on_page:
            for player in players_on_page[player_type]:
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
                item['team'] = response.url.split('/')[-4]
                item['year'] = response.url.split('/')[-2]
                item['roster_status'] = player_type
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
