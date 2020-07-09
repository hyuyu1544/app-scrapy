"""Google Play Spider."""
import scrapy
from datetime import datetime, timedelta
from pyquery import PyQuery
import re
import json
import time

from ..items import AppScrapyItem

class GooglePlay(scrapy.Spider):
    """Google Play Spider."""

    name = 'googleplay'

    def __init__(self, *args, **kwargs):
        """Add additional parameters for spider.

        :params: date (Union[str, None]): crawling date (YYYYMMDD)
        :params: fids (str): comma-separated APP IDs
        :params: comment(boolean)
        """

        date = kwargs.get('date')
        fids = kwargs.get('fids')
        comment = kwargs.get('comment')

        if date:
            self.ignore_time = datetime.strptime(date, '%Y%m%d').date()
        else:
            self.ignore_time = datetime.now().date()

        if fids:
            self.fids = fids.split(',')
        else:
            raise ValueError('fids most be set!')
        if comment == 'True':
            self.crawl_comment=True
        else:
            self.crawl_comment=False


    def start_requests(self):
        """Start Request."""
        
        for fid in self.fids:
            url = f'https://play.google.com/store/apps/details?id={fid}&hl=zh-TW'
            meta = {'fid': fid}
            yield scrapy.Request(
                url=url,
                callback=self.parse_post,
                meta=meta,
            )


    def parse_post(self, response):
        """Parse Post."""

        dom = PyQuery(response.text)
        content_list = []
        for item in dom('div[itemprop="description"] > span[jsslot]').items():
            content_list.append(item.text())
        content = ' 【最新異動】'.join(content_list)
        time = re.search('\d{4}年\d{1,2}月\d{1,2}日', dom(
            '.BgcNfc+.htlgb:first').text()).group(0)
        author = dom('.T32cc.UAO9ie:first > a').text()
        app_name = dom('h1[itemprop="name"]').text()
        yield AppScrapyItem(
            app_name = app_name,
            app_link = response.url,
            author = author,
            content = content,
            created_time =datetime.strptime(time, '%Y年%m月%d日'),
            article_type = 'app',
        )

        # start comments
        if self.crawl_comment:
            comment_page = f'[null,null,[2,2,[40,null,null],null,[]],[\"{response.meta["fid"]}\",7]]'
            dx = ["UsvDTd", comment_page, "null", "generic"]
            data = {
                'f.req': json.dumps([[dx]])
            }
            response.meta['app_name'] = app_name
            yield scrapy.FormRequest(
                url='https://play.google.com/_/PlayStoreUi/data/batchexecute?hl=zh-TW',
                formdata=data,
                callback=self.parse_comment,
                meta=response.meta,
            )


    def parse_comment(self, response):
        """Parse item."""
        try:
            dict_data = json.loads(response.text[4:])
            dict_comment = json.loads(dict_data[0][2])
            for i in dict_comment[0]:
                author = i[1][0]
                content = i[4]
                post_time = datetime.strptime(time.strftime(
                    '%Y-%m-%d %H:%M', time.localtime(i[5][0])), '%Y-%m-%d %H:%M')
                link = f'https://play.google.com/store/apps/details?id={response.meta["fid"]}&reviewId={i[0]}'
                if post_time.date() >= self.ignore_time:
                    yield AppScrapyItem(
                        app_name = response.meta['app_name'],
                        app_link = link,
                        author = author,
                        content = content,
                        created_time =post_time,
                        article_type = 'response',
                    )
                else:
                    return

            next_page = f'[null,null,[2,2,[40,null,{dict_comment[1][1]}],null,[]],[\"{response.meta["fid"]}\",7]]'
            dx = ["UsvDTd", next_page, "null", "generic"]
            next_data = {
                'f.req': json.dumps([[dx]])
            }
            yield scrapy.FormRequest(
                url='https://play.google.com/_/PlayStoreUi/data/batchexecute?hl=zh-TW',
                formdata=next_data,
                callback=self.parse_comment,
                meta=response.meta,
            )
        except IndexError:
            print(f'{response.meta["fid"]} no more comments.')