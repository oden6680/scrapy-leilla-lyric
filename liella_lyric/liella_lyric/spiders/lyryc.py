import scrapy


class LyricSpider(scrapy.Spider):
    name = "lyric"
    allowed_domains = ["www.uta-net.com"]
    start_urls = ["https://www.uta-net.com/artist/30181/5/"]

    def parse(self, response):
        for href in response.css('#list-song > div.row.justify-content-left.mt-lg-4 > div.main.col-sm-12.col-lg-8.flex-grow-1.ms-lg-0.pe-lg-1 > div.row.songlist-table-block.p-3 > div.py-2.p-0.p-lg-2 > table > tbody > tr > td.sp-w-100.pt-0.pt-lg-2 > a::attr(href)'):
            url = 'https://www.uta-net.com' + href.get()
            yield scrapy.Request(url, callback=self.parse_item)
    
    def parse_item(self, response):
        yield {
            'title': response.css('#left-contents > div:nth-child(1) > div > div > div.col-12.col-md > div > div.col-8.col-md-12.my-2 > h2::text').get(),
            'lyricist': response.css('#left-contents > div:nth-child(1) > div > div > div.col-12.col-md > div > div.col-8.align-self-end > p > a:nth-child(1)::text').get(),
            'composer': response.css('#left-contents > div:nth-child(1) > div > div > div.col-12.col-md > div > div.col-8.align-self-end > p > a:nth-child(3)::text').get(),
            'arranger': response.css('#left-contents > div:nth-child(1) > div > div > div.col-12.col-md > div > div.col-8.align-self-end > p > a:nth-child(5)::text').get(),
            'date': ''.join(response.css('#left-contents > div:nth-child(1) > div > div > div.col-12.col-md > div > div.col-8.align-self-end > p::text').getall()).replace(' ','').replace('\n','').replace('\t','')[13:23],
            'lyric': ''.join(response.css('#kashi_area::text').getall())
        }