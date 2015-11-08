from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from dailynews.items import dailynewsItem

class dailynewsspider(CrawlSpider):
    name = "news"
    allowed_domains = ['cnbeta.com']
    start_urls=['http://www.cnbeta.com']
    rules=(Rule(SgmlLinkExtractor(allow=('/articles/.*\.htm', )),callback='parse_page',follow=False),)

    def parse_page(self, response):
        item = dailynewsItem()
        sel = Selector(response)
        item['title']=sel.xpath("//h2/text()").extract()
        item['url']=response.url
        item['content'] = sel.xpath("//section[@class='article_content']").extract()
        #open("t.html",'w').write(item['title'])
        return item
