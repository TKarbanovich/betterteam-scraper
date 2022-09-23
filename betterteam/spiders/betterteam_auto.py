import scrapy


class BetterteamAutoSpider(scrapy.Spider):
    name = 'betterteam-auto'
    allowed_domains = ['www.betterteam.com']
    start_urls = ['https://www.betterteam.com/job-descriptions/page/1']

    def parse(self, response, **kwargs):
        # parse response obj with .xpath
        cards_on_main_page_path = "//div[@class='col-md-6 col-lg-4 card']/div[@class='card-body']"
        card_title_path = ".//h2/a/text()"
        card_short_description_path = ".//div[@class='card-text']/text()"
        card_link_path = ".//h2/a/@href"

        cards_on_page = response.xpath(cards_on_main_page_path)

        for card in cards_on_page:
            card_title = card.xpath(card_title_path).get()

            if 'interview questions' in card_title.lower():
                continue

            card_short_description = card.xpath(card_short_description_path).get()
            card_link = card.xpath(card_link_path).get()

            card_info_main = {
                'title': card_title,
                'short_description': card_short_description,
                'link': card_link,
            }
            yield scrapy.Request(url=card_link, callback=self.parse_inner, meta={'main_key': card_info_main})

        next_page_button = response.xpath("//a[@class='page-link' and @aria-label='Next']/@href").get()
        if next_page_button:
            yield scrapy.Request(url=next_page_button, callback=self.parse)

    @staticmethod
    def parse_inner(response):
        card_info_main = response.request.meta['main_key']

        blue_block_path = "//div[@class='block block-callout primary']"

        long_title_path = ".//p/text()"
        responsibilities_path = ".//ul[1]/li/text()"
        requirements_path = ".//ul[2]/li/text()"

        blue_block = response.xpath(blue_block_path)
        long_title = blue_block.xpath(long_title_path).getall()
        responsibilities = blue_block.xpath(responsibilities_path).getall()
        requirements = blue_block.xpath(requirements_path).getall()

        card_info_inner = {
            'long_title': '\n'.join(long_title),
            'responsibilities': ';'.join(responsibilities),
            'requirements': ';'.join(requirements),
        }

        card_info_main.update(card_info_inner)

        yield card_info_main
