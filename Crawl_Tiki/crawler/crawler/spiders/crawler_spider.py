from scrapy import Spider
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from crawler.items import CrawlerItem


class CrawlerSpider(Spider):
    name = "crawler"
    allowed_domains = ["tiki.vn"]
    start_urls = [
        "https://tiki.vn/dien-thoai-may-tinh-bang/c1789",
    ]
    rules = (
        Rule(LinkExtractor(allow=r"\?page=2"),
             callback="parse_item", follow=True),
    )

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="product-item"]')

        for question in questions:
            question_location = question.xpath('//a/@href').extract()[0]
            full_url = response.urljoin(question_location)
            yield scrapy.Request(full_url, callback=self.parse_question)

    def parse_question(self, response):
        item = CrawlerItem()
        item["title"] = response.xpath(
            '//*[@id="__next"]/div[1]/main/div[2]/div/div[2]/div/div[2]/div[1]/a/span/div/div[3]/div[2]').extract()[0]
        item["url"] = response.url
        item["content"] = response.xpath(
            '//*[@id="__next"]/div[1]/main/div[2]/div/div[2]/div/div[2]/div[1]/a/span/div/div[3]/div[4]/div[1]').extract()[0]
        yield item