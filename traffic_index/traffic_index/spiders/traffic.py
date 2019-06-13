# -*- coding: utf-8 -*-
import scrapy


class TrafficSpider(scrapy.Spider):
    name = "traffic"
    allowed_domains = ["tomtom.com"]
    start_urls = ["https://www.tomtom.com/en_gb/traffic-index/ranking/"]

    def parse(self, response):
        pass
