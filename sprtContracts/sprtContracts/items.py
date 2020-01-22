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
