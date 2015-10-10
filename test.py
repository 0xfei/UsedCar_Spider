# coding=utf-8

from term import Term
from haoche import HaocheSpider
from renrenche import RenrenCheSpider

if __name__ == '__main__':
    spider = RenrenCheSpider()
    spider.get(Term())
    spider = HaocheSpider()
    spider.get(Term())
