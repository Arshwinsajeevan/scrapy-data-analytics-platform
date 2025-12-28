import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes_spider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        quotes = response.css("div.quote")

        for q in quotes:
            yield {
                "quote": q.css("span.text::text").get().strip('“”'),
                "author": q.css("small.author::text").get(),
                "tags": q.css("a.tag::text").getall()
            }

        next_page = response.css("li.next a::attr(href)").get()

        if next_page:
            yield response.follow(next_page, callback=self.parse)
