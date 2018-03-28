# -*- coding: utf-8 -*-
"""
response.css('div.col-md-8 span.text').extract() - gives only the quotes
scrapy crawl quotes -o quotes.json
Created on Fri Nov 17 15:46:52 2017

@author: reety
"""
import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "http://quotes.toscrape.com/page/1/",
    ]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "text": response.selector.xpath(".//html/body/div/div[2]/div[1]/div[1]/span[1]/text()").extract_first(),
                "author": quote.css("small.author::text").extract_first(),
                "tags": quote.css("div.tags a.tag::text").extract(),
            }
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)