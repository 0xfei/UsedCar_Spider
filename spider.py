# coding=utf-8

import requests
import re
from term import Term, Car


class Spider(object):
    def __init__(self, rt='', ru='', rp='', ri='', u='', up=''):
        self.re_type = rt
        self.re_url = ru
        self.re_price = rp
        self.re_items = ri
        self.url_base = u
        self.url_price = up

    def get_description(self, detail):
        pass

    def get_time_distance(self, i):
        pass

    def parse(self, content):
        items = re.findall(self.re_items, content)
        for i in items:
            car = Car()
            car.address = (self.url_base + re.findall(self.re_url, i)[0])
            car.type = re.findall(self.re_type, i)[0].strip()
            car.price = re.findall(self.re_price, i)[0]
            (car.time, car.distance) = self.get_time_distance(i)
            try:
                detail = requests.get(car.address).content
                if not detail:
                    break
                if detail.find("国三") != -1:
                    car.gas = 3
                car.description = self.get_description(detail)
            except Exception as e:
                print e.message
                break
            print 'Car:%s, Price: %s, Time: %s, Distance: %s, Gas: %d, Desc: %s ' % \
                  (car.type, car.price, car.time, car.distance, car.gas, car.description)
        return len(items)

    def get(self, term):
        if isinstance(term, Term):
            try:
                page = 1
                while True:
                    url = self.url_price % (term.city, term.low_money, term.high_money, page)
                    home = requests.get(url)
                    if not self.parse(home.content):
                        break
                    page += 1
            except Exception as e:
                print e.message
