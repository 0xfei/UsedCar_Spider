__author__ = 'liuyufei'


class Term:
    def __init__(self, lm=0, hm=5, t='', ly=0, hy=5, d=10, c='cd'):
        self.low_money = lm
        self.high_money = hm
        self.type = t
        self.low_year = ly
        self.high_year = hy
        self.distance = d
        self.city = c

    def set_money(self, f, t):
        self.low_money = f
        self.high_money = t

    def set_type(self, t):
        self.type = t

    def set_year(self, f, t):
        self.low_year = f
        self.high_year = t

    def set_distance(self, limit):
        self.distance = limit

    def set_city(self, c):
        self.city = c


class Car:
    def __init__(self):
        self.url = r''
        self.year = 0
        self.price = 0
        self.type = ''
        self.distance = 0
        self.number = 0
        self.good = 0
        self.emergency = 0
        self.hash = 0
        self.gas = 4
        self.description = ''
