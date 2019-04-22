import scrapy
from tutorialn.items import DmozItem

class DmozSpider(scrapy.Spider):
  name='dmoz'
  allowed_domains = ['http://dmoz-odp.org']
  start_urls = [
    'http://dmoz-odp.org/Computers/Programming/Languages/Python/Books/',
    'http://dmoz-odp.org/Computers/Programming/Languages/Python/Resources'
    ]
  def parse(self, response):
    filename = response.url.split("/")[-2]
    for sel in response.xpath('//ul/li'):
      item = DmozItem()
      item['title'] = sel.xpath('a/text()').extract()
      item['link'] = sel.xpath('a/@href').extract()
      item['desc'] = sel.xpath('text()').extract()
      yield item
