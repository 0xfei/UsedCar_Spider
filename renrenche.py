# coding=utf-8

import requests
from term import Term, Car
import re


def parser(content):
    items = re.findall(r'list-item">([\s\S]*?)</li>', content)
    for i in items:
        car = Car()
        car.url = ('http://www.renrenche.com' + re.findall(r'href="(.*?)"', i)[0])
        car.type = re.findall(r'<p>(.*?)</p>', i)[0].strip()
        car.price = re.findall(r'<div class="price">(.*?)<span>', i)[0]
        temp = re.findall(r'<span class="basic">(.*?)<em class="separator">/</em>(.*)</span>', i)[0]
        car.time = temp[0]
        car.distance = temp[1]
        try:
            detail = requests.get(car.url).content
            if not detail:
                break
            if detail.find("国三") != -1:
                car.gas = 3
            goods = re.findall('<p class="sub-title">([\s\S]*?)</p>', detail)
            for good in goods:
                car.description += ','.join(re.findall(r'<span(?:[\s\S]*?)>([\s\S]*?)</span>', good))
        except Exception as e:
            print e.message
        print 'Car:%s, Price: %s, Time: %s, Distance: %s, Gas: %d, desp: %s ' % \
              (car.type, car.price, car.time, car.distance, car.gas, car.description)
    return len(items)


def get_renrenche(term):
    if isinstance(term, Term):
        url = r'http://www.renrenche.com/%s/%d-%dwan' % \
              (term.city, term.low_money, term.high_money)
        try:
            page = 1
            while True:
                home = requests.get(url+'/p'+str(page))
                if not parser(home.content):
                    break
                page += 1
        except Exception as e:
            print e.message
