# -*- coding: utf-8 -*-
import scrapy
from ..items import ScrapItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        items = ScrapItem()
        all_div_quote = response.css('div.quote')
        for quote in all_div_quote:
            author = quote.css(".author::text").extract()
            title = quote.css(".text::text").extract()
            tag = quote.css('.tags .tag::text').extract()
            items['title'] = title
            items['author'] = author
            items['tag'] = tag
            yield items

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
