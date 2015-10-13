class Term:
    def __init__(self, lm=0, hm=5, t='', ly=0, hy=5, d=10, c='cd'):
        self.low_money = lm
        self.high_money = hm
        self.type = t
        self.low_year = ly
        self.high_year = hy
        self.distance = d
        self.city = c


class Car:
    def __init__(self):
        self.address = ''
        self.year = 0
        self.price = 0
        self.type = ''
        self.time = ''
        self.distance = 0
        self.gas = 4
        self.description = ''
