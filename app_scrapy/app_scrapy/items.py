"""Items."""

import scrapy


class AppScrapyItem(scrapy.Item):
    """Define the fields for AppScrapy item here."""

    app_name = scrapy.Field()
    app_link = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()
    created_time = scrapy.Field()
    article_type = scrapy.Field()

