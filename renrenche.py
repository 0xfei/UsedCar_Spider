# coding=utf-8

from spider import Spider
import re

class RenrenCheSpider(Spider):
    def __init__(self):
        super(RenrenCheSpider, self).__init__(
            rt=r'<p>(.*?)</p>',
            ru=r'href="(.*?)"',
            rp=r'<div class="price">(.*?)<span>',
            ri=r'list-item">([\s\S]*?)</li>',
            u=r'http://www.renrenche.com',
            up=r'http://www.renrenche.com/%s/%d-%dwan/p%d'
        )

    def get_description(self, detail):
        goods = re.findall('<p class="sub-title">([\s\S]*?)</p>', detail)
        return ','.join([','.join(re.findall(r'<span(?:[\s\S]*?)>([\s\S]*?)</span>', good)) for good in goods])

    def get_time_distance(self, i):
        return re.findall(
            r'<span class="basic">(.*?)<em class="separator">/</em>(.*)</span>',
            i)[0]
