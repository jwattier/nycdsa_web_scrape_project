# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SprtcontractsItem (scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    position = scrapy.Field()
    team = scrapy.Field()
    currentAge = scrapy.Field()
    totalYears = scrapy.Field()
    totalAmount = scrapy.Field()
    avgAmount = scrapy.Field()
    grtAmount = scrapy.Field()
    practicalGrt = scrapy.Field()
    grtSigning = scrapy.Field()
    faYear = scrapy.Field()
    yrRange = scrapy.Field()
    ageAtBeg = scrapy.Field()


class NflteamItem (scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    year = scrapy.Field()
    team = scrapy.Field()
    roster_status = scrapy.Field()
    name = scrapy.Field()
    position = scrapy.Field()
    base_salary = scrapy.Field()
    signing_bonus = scrapy.Field()
    roster_bonus = scrapy.Field()
    option_bonus = scrapy.Field()
    workout_bonus = scrapy.Field()
    restruct_bonus = scrapy.Field()
    other_bonus = scrapy.Field()
    dead_cap_amt = scrapy.Field()
    cap_hit = scrapy.Field()
    cap_perc = scrapy.Field()