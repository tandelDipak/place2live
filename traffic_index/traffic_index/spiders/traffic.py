# -*- coding: utf-8 -*-
import scrapy


class TrafficSpider(scrapy.Spider):
    name = "traffic"
    allowed_domains = ["tomtom.com"]
    start_urls = ["https://www.tomtom.com/en_gb/traffic-index/ranking/"]

    def parse(self, response):
        xpath_selector = "//*[@id='RankingPage-table']//table//tr/td[{}]"
        world_ranks = response.xpath(xpath_selector.format(1)).getall()
        cities = response.xpath(xpath_selector.format(3)).getall()
        countries = response.xpath(xpath_selector.format(4)).getall()
        congestion_levels = response.xpath(xpath_selector.format(5)).getall()
        for rank, city, country, level in zip(world_ranks, cities, countries, congestion_levels):
            i = ItemLoader(item=TrafficIndexItem())
            i.add_value("world_rank", rank)
            i.add_value("city", city)
            i.add_value("country", country)
            i.add_value("congestion_level", level)
            yield i.load_item()
