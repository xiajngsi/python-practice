import scrapy
class DmozSpider(scrapy.Spider):
  name='dmoz'
  allowed_domains = ['http://dmoz-odp.org']
  start_urls = [
    'http://dmoz-odp.org/Computers/Programming/Languages/Python/Books/',
    'http://dmoz-odp.org/Computers/Programming/Languages/Python/Resources'
    ]
  def parse(self, response):
    filename = response.url.split("/")[-2]
    with open(filename, 'wb') as f:
      f.write(response.body)
